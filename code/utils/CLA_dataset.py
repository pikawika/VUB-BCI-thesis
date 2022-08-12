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
from tabnanny import verbose
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
        
class ImportantMarker:
    def __init__(self, mark, old_mark, start_idx, end_idx):
        self.mark = mark
        self.old_mark = old_mark
        self.start_idx = start_idx
        self.end_idx = end_idx

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


# Link event ID (marker) with a textual description
marker_to_textual_dict = {0: "info/blank_screen",
                          1: "task/left",
                          2: "task/right",
                          3: "task/neutral",
                          91: "info/inter_session_break",
                          92: "info/experiment_end",
                          99: "info/initial_relaxation"}

motor_cortex_electrodes = ["T3", "C3", "Cz", "C4", "T4"]

# Make a dictionary linking description with a marker (inverse of marker_to_textual_dict)
textual_to_marker_dict = {value: key for key, value in marker_to_textual_dict.items()}

# Usefull MI event IDs
usefull_mi_marker_to_textual_dict = {"task/left": 1,
                                     "task/right": 2,
                                     "task/neutral": 3}

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
    mne_file = mne.io.Raw(filename, verbose=False)

    return mne_file

def get_raw_mne_data_for_subject(subject_id):
    """Gets raw mne data structure for given subject."""
    # Example call: CLA_dataset.get_raw_mne_data("C")
    
    # Find all filenames for subject
    filenames = [filename for filename in mne_filenames if f"Subject{subject_id}" in filename]
    if (not filenames):
        raise ValueError("No files for provided subject ID")
    
    # Check file availability
    if (not check_mne_files_availability()):
        raise ValueError("Some mne files are not available in data directory")
    
    mne_files = []
    
    for filename in filenames:
        # Get full mne file
        mne_files.append(mne.io.Raw(filename, verbose=False))

    return mne_files

def get_all_raw_mne_data_for_subject(subject_id):
    """
    Gets all raw mne data structures for given subject and loads it in memory.
    Returns a list of loaded MNE objects
    """
    return [raw.load_data() for raw in get_raw_mne_data_for_subject(subject_id)]

def get_specific_raw_mne_data_for_subject(subject_id, index: int):
    """
    Gets the MNE raw of a subject at the provided index and loads it into memory.
    Returns a loeded MNE object.
    """
    mne_raws = get_raw_mne_data_for_subject(subject_id)
    if (len(mne_raws) > index and 0 <= index):
        # Valid index
        return mne_raws[index].load_data()
    else:
        raise ValueError(f"There is no MNE raw at the provided index {index} for the subject {subject_id}") 

def get_last_raw_mne_data_for_subject(subject_id):
    """
    Gets the MNE raw of a subject with the latest recording date.
    This could be seen as the last session a user performed.
    """
    # Get all MNE raws
    mne_raws = get_raw_mne_data_for_subject(subject_id)
    
    # Find newest MNE
    newest_mne_raw = mne_raws[0]
    for mne_raw in mne_raws:
        if mne_raw.info["meas_date"] > newest_mne_raw.info["meas_date"]:
            # New ones date is bigger a.k.a. more recent
            newest_mne_raw = mne_raw
            
    # Return newest mne raw
    return newest_mne_raw.load_data()

def get_all_but_last_raw_mne_data_for_subject(subject_id):
    """
    Gets the MNE raws of a subject except for the one with the latest recording date.
    This could be seen as all sessions except for the last one.
    """
    # Get all MNE raws
    mne_raws = get_raw_mne_data_for_subject(subject_id)
    
    # List of accepted MNE raws
    return_list = []
    
    # Find newest MNE
    newest_mne_raw = mne_raws[0].load_data()
    for mne_raw in mne_raws:
        mne_raw.load_data()
        if mne_raw.info["meas_date"] > newest_mne_raw.info["meas_date"]:
            # New ones date is bigger a.k.a. more recent, previous one may be included in data
            return_list.append(newest_mne_raw)
            
            # Current raw is new "last" so should not be included
            newest_mne_raw = mne_raw
        else:
            # Only add if not our current one (i.e. our initial one set)
            if (newest_mne_raw !=  mne_raw):
                return_list.append(mne_raw)
            
    
            
    # Return newest mne raw
    return return_list

def get_important_markers(filename):
    """Gets important markers for given filename."""
    # Example call: get_important_markers("CLASubjectC1511263StLRHand")
    
    data_markers = get_raw_matlab_data(filename).marker
    
    # Initial values
    important_markers = []
    new_mark = old_mark = start_idx = end_indx = -1

    for idx, marker in enumerate(data_markers):
        # Initial values
        if (start_idx == -1):
            start_idx = idx
            new_mark = old_mark = marker
            
        # Change of marker
        if (marker != new_mark):
            # Save marker
            end_indx = idx - 1
            important_markers.append(ImportantMarker(new_mark, old_mark, start_idx, end_indx))
            
            # Start new marker
            old_mark = new_mark
            new_mark = marker
            start_idx = idx
            
    # End of loop, create last record if needed
    if (start_idx > end_indx):
        # Save marker
        end_indx = idx
        important_markers.append(ImportantMarker(new_mark, old_mark, start_idx, end_indx))
        
    # Return important markers
    return important_markers

def get_events_and_dict_from_annotated_raw(raw_mne):
    """Gets events from annotations in a RAW MNE object. Returns events followed by the used dict."""
    # Example call: mne_events, mne_event_conversion_used_dict = get_important_markers("CLASubjectC1511263StLRHand")
    
    return mne.events_from_annotations(raw_mne, event_id=textual_to_marker_dict, verbose=False)

def get_usefull_epochs_from_raw(raw_mne, start_offset=-0.2, end_offset=0.2, baseline=(0, 1)):
    """Gets epochs from raw epoch with the ability to specify the offset on the start and of the evoked signal"""
    
    # Get events
    mne_events, _ = get_events_and_dict_from_annotated_raw(raw_mne)
    
    # Return the epochs
    return mne.Epochs(raw= raw_mne, events= mne_events,
                      event_id= usefull_mi_marker_to_textual_dict,
                      baseline= baseline,
                      verbose= False,
                      tmin= (0 + start_offset), tmax= (1 + end_offset))
