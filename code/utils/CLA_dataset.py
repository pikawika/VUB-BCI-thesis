# This util file has some basic operations for the CLA dataset.
# Some of these operations were extracted from the expiremental CLA dataset exploration notebook

# Import it as follows:
# | import sys
# | sys.path.append('../utils')
# | import CLA_dataset

# --------------- IMPORTS ---------------
# Performs IO operations
import os
import scipy.io

# Modules tailored for EEG data
import mne

# Data manipulation modules
import numpy as np

# Datetime object
import datetime
import pytz

# --------------- CLASSES ---------------


class MetaData:
    def __init__(self, record_date, sex, age):
        self.record_date = record_date
        self.sex = sex
        self.age = age


# --------------- GLOBALS ---------------
data_directory = r'../data/CLA/'
filenames = ["CLA-SubjectJ-170504-3St-LRHand-Inter.mat",
             "CLA-SubjectJ-170508-3St-LRHand-Inter.mat",
             "CLA-SubjectJ-170510-3St-LRHand-Inter.mat",
             "CLASubjectA1601083StLRHand.mat",
             "CLASubjectB1510193StLRHand.mat",
             "CLASubjectB1512153StLRHand.mat",
             "CLASubjectC1511263StLRHand.mat",
             "CLASubjectC1512163StLRHand.mat",
             "CLASubjectC1512233StLRHand.mat",
             "CLASubjectD1511253StLRHand.mat",
             "CLASubjectE1512253StLRHand.mat",
             "CLASubjectE1601193StLRHand.mat",
             "CLASubjectE1601223StLRHand.mat",
             "CLASubjectF1509163StLRHand.mat",
             "CLASubjectF1509173StLRHand.mat",
             "CLASubjectF1509283StLRHand.mat"]


meta_data = [
    # CLA-SubjectJ-170504-3St-LRHand-Inter.mat
    MetaData(datetime.datetime(2017, 5, 4, 0, 0,
             0, 0, pytz.UTC).timestamp(), 2, 25),
    # CLA-SubjectJ-170508-3St-LRHand-Inter.mat
    MetaData(datetime.datetime(2017, 5, 8, 0, 0,
             0, 0, pytz.UTC).timestamp(), 2, 25),
    # CLA-SubjectJ-170510-3St-LRHand-Inter.mat
    MetaData(datetime.datetime(2017, 5, 10, 0, 0,
             0, 0, pytz.UTC).timestamp(), 2, 25),
    # CLASubjectA1601083StLRHand.mat
    MetaData(datetime.datetime(2016, 1, 8, 0, 0,
             0, 0, pytz.UTC).timestamp(), 1, 25),
    # CLASubjectB1510193StLRHand.mat
    MetaData(datetime.datetime(2015, 10, 19, 0, 0,
             0, 0, pytz.UTC).timestamp(), 1, 25),
    # CLASubjectB1512153StLRHand.mat
    MetaData(datetime.datetime(2015, 12, 15, 0, 0,
             0, 0, pytz.UTC).timestamp(), 1, 25),
    # CLASubjectC1511263StLRHand.mat
    MetaData(datetime.datetime(2015, 11, 26, 0, 0,
             0, 0, pytz.UTC).timestamp(), 1, 30),
    # CLASubjectC1512163StLRHand.mat
    MetaData(datetime.datetime(2015, 12, 16, 0, 0,
             0, 0, pytz.UTC).timestamp(), 1, 30),
    # CLASubjectC1512233StLRHand.mat
    MetaData(datetime.datetime(2015, 12, 23, 0, 0,
             0, 0, pytz.UTC).timestamp(), 1, 30),
    # CLASubjectD1511253StLRHand.mat
    MetaData(datetime.datetime(2015, 11, 25, 0, 0,
             0, 0, pytz.UTC).timestamp(), 1, 30),
    # CLASubjectE1512253StLRHand.mat
    MetaData(datetime.datetime(2015, 12, 25, 0, 0,
             0, 0, pytz.UTC).timestamp(), 2, 25),
    # CLASubjectE1601193StLRHand.mat
    MetaData(datetime.datetime(2016, 1, 19, 0, 0,
             0, 0, pytz.UTC).timestamp(), 2, 25),
    # CLASubjectE1601223StLRHand.mat
    MetaData(datetime.datetime(2016, 1, 23, 0, 0,
             0, 0, pytz.UTC).timestamp(), 2, 25),
    # CLASubjectF1509163StLRHand.mat
    MetaData(datetime.datetime(2015, 9, 16, 0, 0,
             0, 0, pytz.UTC).timestamp(), 1, 35),
    # CLASubjectF1509173StLRHand.mat
    MetaData(datetime.datetime(2015, 9, 17, 0, 0,
             0, 0, pytz.UTC).timestamp(), 1, 35),
    # CLASubjectF1509283StLRHand.mat
    MetaData(datetime.datetime(2015, 9, 28, 0, 0, 0, 0, pytz.UTC).timestamp(), 1, 35)]


# --------------- FUNCTIONS ---------------


def check_file_availability():
    """Checks if all CLA files are available."""
    # Example call: CLA_dataset.check_file_availability()
    all_files_available = True

    for filename in filenames:
        if (not os.path.isfile(data_directory + filename)):
            print(data_directory + filename + "not available!")
            all_files_available = False

    return all_files_available


def is_correct_filename(filename):
    """Checks if provided filename is valid CLA filename."""
    # Example call: CLA_dataset.is_correct_filename("CLASubjectC1511263StLRHand.mat")
    return filename in filenames


def get_raw_matlab_data(filename):
    """Gets raw matlab data for given filename."""
    # Example call: CLA_dataset.get_raw_mne_data("CLASubjectC1511263StLRHand.mat")
    if (not is_correct_filename(filename)):
        raise ValueError("File does not exist")

    # Get full matlab file
    data_raw_full = scipy.io.loadmat(
        data_directory + filename, struct_as_record=False, squeeze_me=True)

    # The data is stored inside the matlab structure named "o"
    data_raw = data_raw_full['o']

    return data_raw


def get_raw_mne_data(filename):
    """Gets raw mne data structure for given filename."""
    # Example call: CLA_dataset.get_raw_mne_data("CLASubjectC1511263StLRHand.mat", datetime.datetime(2016, 1, 8, 0, 0, 0, 0, pytz.UTC).timestamp(), 1)
    if (not is_correct_filename(filename)):
        raise ValueError("File does not exist")
    
    # Index of file
    index = filenames.index(filename)

    # Correct date format
    recording_date = datetime.datetime.fromtimestamp(
        meta_data[index].record_date, tz=datetime.timezone.utc)

    # Get raw matlab file
    data_raw = get_raw_matlab_data(filename)

    # Create MNE info object
    mne_ch_names = data_raw.chnames.tolist()
    mne_ch_names.pop(-1)
    mne_ch_types = ['eeg'] * len(mne_ch_names)
    mne_sfreq = data_raw.sampFreq

    mne_info = mne.create_info(
        ch_names=mne_ch_names, ch_types=mne_ch_types, sfreq=mne_sfreq)

    # Set other fields of MNE info object
    mne_info.set_montage('standard_1020')
    mne_info['description'] = 'Data from ' + filename
    mne_info['experimenter'] = 'Kaya et al.'
    mne_info['meas_date'] = recording_date
    mne_info['subject_info'] = {
        "his_id": data_raw.id,
        "sex": meta_data[index].sex
    }

    # Make MNE data
    mne_raw_data = data_raw.data
    mne_raw_data = mne_raw_data[:, :-1]
    mne_raw_data = mne_raw_data.transpose()

    # Make MNE array
    mne_raw = mne.io.RawArray(mne_raw_data, mne_info)
    return mne_raw
