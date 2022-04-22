# This util file has some basic operations for the CLA dataset.
# Some of these operations were extracted from the expiremental CLA dataset exploration notebook

# Import it as follows:
# | import sys
# | sys.path.append('../utils')
# | import CLA_dataset

##################################
# IMPORTS
##################################

# Performs IO operations
import os
import scipy.io # 1.8.0 recommended

# Modules tailored for EEG data
import mne # 1.0.2 recommended

# Data manipulation modules
import numpy as np # 1.21.5 recommended

# Datetime object
import datetime
import pytz

##################################
# CLASSES
##################################


class MneDataInfo:
    def __init__(self, file_location, subject, date_of_recording, sex, age, health_condition, prior_bci_experience, bci_literacy):
        self.file_location = file_location
        self.subject = subject
        self.date_of_recording = date_of_recording
        self.sex = sex
        self.age = age
        self.health_condition = health_condition
        self.prior_bci_experience= prior_bci_experience
        self.bci_literacy = bci_literacy

##################################
# GLOBALS 
##################################

# Prefix to data directory
data_dir = "../data/CLA/"

# Create data information for each usefull record
meta_data_list = [
    # CLASubjectA1601083StLRHand.mat
    MneDataInfo(file_location= data_dir + "CLASubjectA1601083StLRHand.mat",
                subject= "A",
                date_of_recording= datetime.datetime(2016, 1, 8, 0, 0, 0, 0, pytz.UTC),
                sex= "M",
                age= 25,
                health_condition= "Healthy",
                prior_bci_experience = False,
                bci_literacy= "Intermediate - High"),
    
    # CLASubjectB1510193StLRHand.mat
    MneDataInfo(file_location= data_dir + "CLASubjectB1510193StLRHand.mat",
                subject= "B",
                date_of_recording= datetime.datetime(2015, 10, 19, 0, 0, 0, 0, pytz.UTC),
                sex= "M",
                age= 25,
                health_condition= "Healthy",
                prior_bci_experience = False,
                bci_literacy= "Intermediate - Low"),
    
    # CLASubjectB1510203StLRHand.mat
    MneDataInfo(file_location= data_dir + "CLASubjectB1510203StLRHand.mat",
                subject= "B",
                date_of_recording= datetime.datetime(2015, 10, 20, 0, 0, 0, 0, pytz.UTC),
                sex= "M",
                age= 25,
                health_condition= "Healthy",
                prior_bci_experience = False,
                bci_literacy= "Intermediate - Low"),
    
    # CLASubjectB1512153StLRHand.mat
    MneDataInfo(file_location= data_dir + "CLASubjectB1512153StLRHand.mat",
                subject= "B",
                date_of_recording= datetime.datetime(2015, 12, 15, 0, 0, 0, 0, pytz.UTC),
                sex= "M",
                age= 25,
                health_condition= "Healthy",
                prior_bci_experience = False,
                bci_literacy= "Intermediate - Low"),
    
    # CLASubjectC1511263StLRHand.mat
    MneDataInfo(file_location= data_dir + "CLASubjectC1511263StLRHand.mat",
                subject= "C",
                date_of_recording= datetime.datetime(2015, 11, 26, 0, 0, 0, 0, pytz.UTC),
                sex= "M",
                age= 30,
                health_condition= "Healthy",
                prior_bci_experience = False,
                bci_literacy= "Intermediate - High"),
    
    # CLASubjectC1512163StLRHand.mat
    MneDataInfo(file_location= data_dir + "CLASubjectC1512163StLRHand.mat",
                subject= "C",
                date_of_recording= datetime.datetime(2015, 12, 16, 0, 0, 0, 0, pytz.UTC),
                sex= "M",
                age= 30,
                health_condition= "Healthy",
                prior_bci_experience = False,
                bci_literacy= "Intermediate - High"),
    
    # CLASubjectC1512233StLRHand.mat
    MneDataInfo(file_location= data_dir + "CLASubjectC1512233StLRHand.mat",
                subject= "C",
                date_of_recording= datetime.datetime(2015, 12, 23, 0, 0, 0, 0, pytz.UTC),
                sex= "M",
                age= 30,
                health_condition= "Healthy",
                prior_bci_experience = False,
                bci_literacy= "Intermediate - High"),
    
    # CLASubjectD1511253StLRHand.mat
    MneDataInfo(file_location= data_dir + "CLASubjectD1511253StLRHand.mat",
                subject= "D",
                date_of_recording= datetime.datetime(2015, 11, 25, 0, 0, 0, 0, pytz.UTC),
                sex= "M",
                age= 30,
                health_condition= "Healthy",
                prior_bci_experience = False,
                bci_literacy= "Intermediate - Low"),
    
    # CLASubjectE1512253StLRHand.mat
    MneDataInfo(file_location= data_dir + "CLASubjectE1512253StLRHand.mat",
                subject= "E",
                date_of_recording= datetime.datetime(2015, 12, 25, 0, 0, 0, 0, pytz.UTC),
                sex= "F",
                age= 25,
                health_condition= "Healthy",
                prior_bci_experience = False,
                bci_literacy= "Intermediate - Low"),
    
    # CLASubjectE1601193StLRHand.mat
    MneDataInfo(file_location= data_dir + "CLASubjectE1601193StLRHand.mat",
                subject= "E",
                date_of_recording= datetime.datetime(2016, 1, 19, 0, 0, 0, 0, pytz.UTC),
                sex= "F",
                age= 25,
                health_condition= "Healthy",
                prior_bci_experience = False,
                bci_literacy= "Intermediate - Low"),
    
    # CLASubjectE1601223StLRHand.mat
    MneDataInfo(file_location= data_dir + "CLASubjectE1601223StLRHand.mat",
                subject= "E",
                date_of_recording= datetime.datetime(2016, 1, 22, 0, 0, 0, 0, pytz.UTC),
                sex= "F",
                age= 25,
                health_condition= "Healthy",
                prior_bci_experience = False,
                bci_literacy= "Intermediate - Low"),
    
    # CLASubjectF1509163StLRHand.mat - removed due to only 2 recorded signals
    
    # CLASubjectF1509173StLRHand.mat
    MneDataInfo(file_location= data_dir + "CLASubjectF1509173StLRHand.mat",
                subject= "F",
                date_of_recording= datetime.datetime(2015, 9, 17, 0, 0, 0, 0, pytz.UTC),
                sex= "M",
                age= 35,
                health_condition= "Healthy",
                prior_bci_experience = False,
                bci_literacy= "Intermediate - Low"),
    
    # CLASubjectF1509283StLRHand.mat
    MneDataInfo(file_location= data_dir + "CLASubjectF1509283StLRHand.mat",
                subject= "F",
                date_of_recording= datetime.datetime(2015, 9, 28, 0, 0, 0, 0, pytz.UTC),
                sex= "M",
                age= 35,
                health_condition= "Healthy",
                prior_bci_experience = False,
                bci_literacy= "Intermediate - Low"),
]

# Matlab filenames of CLA
matlab_filenames = [data_dir + "CLASubjectA1601083StLRHand.mat",
                    data_dir + "CLASubjectB1510193StLRHand.mat",
                    data_dir + "CLASubjectB1510203StLRHand.mat",
                    data_dir + "CLASubjectB1512153StLRHand.mat",
                    data_dir + "CLASubjectC1511263StLRHand.mat",
                    data_dir + "CLASubjectC1512163StLRHand.mat",
                    data_dir + "CLASubjectC1512233StLRHand.mat",
                    data_dir + "CLASubjectD1511253StLRHand.mat",
                    data_dir + "CLASubjectE1512253StLRHand.mat",
                    data_dir + "CLASubjectE1601193StLRHand.mat",
                    data_dir + "CLASubjectE1601223StLRHand.mat",
                    data_dir + "CLASubjectF1509163StLRHand.mat",
                    data_dir + "CLASubjectF1509173StLRHand.mat",
                    data_dir + "CLASubjectF1509283StLRHand.mat"]

# MNE stored file names
mne_filenames = [data_dir + "CLASubjectA1601083StLRHand_raw.fif",
                 data_dir + "CLASubjectB1510193StLRHand_raw.fif",
                 data_dir + "CLASubjectB1510203StLRHand_raw.fif",
                 data_dir + "CLASubjectB1512153StLRHand_raw.fif",
                 data_dir + "CLASubjectC1511263StLRHand_raw.fif",
                 data_dir + "CLASubjectC1512163StLRHand_raw.fif",
                 data_dir + "CLASubjectC1512233StLRHand_raw.fif",
                 data_dir + "CLASubjectD1511253StLRHand_raw.fif",
                 data_dir + "CLASubjectE1512253StLRHand_raw.fif",
                 data_dir + "CLASubjectE1601193StLRHand_raw.fif",
                 data_dir + "CLASubjectE1601223StLRHand_raw.fif",
                 data_dir + "CLASubjectF1509173StLRHand_raw.fif",
                 data_dir + "CLASubjectF1509283StLRHand_raw.fif"]

##################################
# FUNCTIONS
##################################


def check_matlab_files_availability():
    """Checks if all matlab CLA files are available."""
    # Example call: CLA_dataset.check_matlab_files_availability()
    all_files_available = True

    for filename in matlab_filenames:
        if (not os.path.isfile(filename)):
            print("Matlab file not available: " + filename)
            all_files_available = False

    return all_files_available

def check_mne_files_availability():
    """Checks if all MNE fif CLA files are available."""
    # Example call: CLA_dataset.check_mne_files_availability()
    all_files_available = True

    for filename in mne_filenames:
        if (not os.path.isfile(filename)):
            print("MNE file not available: " + filename)
            all_files_available = False

    return all_files_available


def is_correct_matlab_filename(filename):
    """Checks if provided filename is valid matlab CLA filename."""
    # Example call: CLA_dataset.is_correct_matlab_filename("../data/CLA/CLASubjectC1511263StLRHand.mat")
    return filename in matlab_filenames


def is_correct_mne_filename(filename):
    """Checks if provided filename is valid MNE fif CLA filename."""
    # Example call: CLA_dataset.is_correct_mne_filename("../data/CLA/CLASubjectA1601083StLRHand_raw.fif")
    return filename in mne_filenames


def get_raw_matlab_data(filename):
    """Gets raw matlab data for given filename."""
    # Example call: CLA_dataset.get_raw_matlab_data("CLASubjectC1511263StLRHand")
    
    # Make filename a matlab filename
    filename = data_dir + filename + ".mat"
    
    # Check file availability
    if (not check_matlab_files_availability()):
        raise ValueError("Some matlab files are not available in data directory")
        
    # Check filename correct
    if (not is_correct_matlab_filename(filename)):
        raise ValueError("Filename not a valid matlab CLA filename")

    # Get full matlab file
    data_raw_full = scipy.io.loadmat(
        filename, struct_as_record=False, squeeze_me=True)

    # The data is stored inside the matlab structure named "o"
    data_raw = data_raw_full['o']

    return data_raw


def get_raw_mne_data(filename):
    """Gets raw mne data structure for given filename."""
    # Example call: CLA_dataset.get_raw_mne_data("CLASubjectC1511263StLRHand")
    
    # Make filename a MNE filename
    filename = data_dir + filename + "_raw.fif"
    
    # Check file availability
    if (not check_mne_files_availability()):
        raise ValueError("Some mne files are not available in data directory")
        
    # Check filename correct
    if (not is_correct_mne_filename(filename)):
        raise ValueError("Filename not a valid mne CLA filename")

    # Get full mne file
    mne_file = mne.io.Raw(filename)

    return mne_file
