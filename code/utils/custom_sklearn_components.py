# This util provides some SKLearn specific helper functions.

# Import it as follows:
# | import sys
# | sys.path.append('../utils')
# | import custom_sklearn_components

##################################
# IMPORTS
##################################

# SKLearn
import sklearn
from sklearn.base import BaseEstimator,TransformerMixin

# Deep copy
import copy

# MNE for filter
import mne

# np for data control
import numpy as np

# IO functions
from IPython.utils import io

####################################################
# PROVIDE FILTER AS SKLEARN COMPATIBLE OBJECT
####################################################

class EpochsToFilteredData(BaseEstimator,TransformerMixin):
    """
    Transforms the inputed data by filtering it using an overlap-add IIR filter with the provided lower and upper bound.
    Returns the slice of the requested data in tmin tmax format in same fashion as MNE.
    SKlearn pipeline compatible but assumes MNE Epochs are passed in a loaded manner.
    """
    def __init__(self, start_offset,
                 data_tmin, data_tmax,
                 sfreq= 200, filter_lower_bound= 2, 
                 filter_upper_bound= 32):
        """
        Please provide the:
        - start_offset: start time of the data epoch, in seconds from the queue onset
        - end_offset: end time of the data epoch, in seconds from the queue onset
        - data_tmin: start time of the data to be returned, in seconds from the queue onset
        - data_tmax: end time of the data to be returned, in seconds from the queue onset
        - sfreq: sampling frequency (default: CLA dataset sampling frequency of 200)
        - filter_lower_bound: lower bound for the filter in Hz (default: 2)
        - filter_upper_bound: lower bound for the filter in Hz (default: 32)
        """
        self.start_offset = start_offset
        self.data_tmin = data_tmin
        self.data_tmax = data_tmax
        self.filter_lower_bound = filter_lower_bound
        self.filter_upper_bound = filter_upper_bound
        self.sfreq = sfreq

    def fit(self, X, y=None):
        """
        Dummy function needed for SKlearn
        """
        # There is no real fitting of the filter needed
        return self
    
    def transform(self, X, y=None):
        """
        Transforms the inputed epochs by first filtering it using an overlap-add FIR filter with the provided lower and upper bound and then returning only the data in window of interest.
        """
        # Filter on complete data
        filtered = mne.filter.filter_data(data=X,
                                          sfreq= self.sfreq,
                                          l_freq = self.filter_lower_bound,
                                          h_freq = self.filter_upper_bound,
                                          picks= None,
                                          phase= "minimum",
                                          fir_window= "blackman",
                                          fir_design= "firwin",
                                          pad= 'median',
                                          verbose= False)
        
        # Determine zero point, aka true seconds in epoch where queue onset is
        zero_point_time = 0 - self.start_offset
        
        # Determine the index of data_tmin
        start_time = zero_point_time + self.data_tmin
        start_index = np.round(start_time * self.sfreq).astype(int)
        
        # Determine the index of data_tmax
        end_time = zero_point_time + self.data_tmax
        end_index = np.round(end_time * self.sfreq).astype(int)
        
        # Return list, carefull data is 3D [epoch_id, electrode_id, data]
        return_list = [[l3[start_index:end_index] for l3 in l2] for l2 in filtered]
        
        # Return the sliced data
        return return_list
