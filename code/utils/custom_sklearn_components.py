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

# IO functions
from IPython.utils import io

####################################################
# PROVIDE FILTER AS SKLEARN COMPATIBLE OBJECT
####################################################

class EpochsToFilteredData(BaseEstimator,TransformerMixin):
    """
    Transforms the inputed epochs by first filtering it using an overlap-add FIR filter with the provided lower and upper bound and then returning only the data in window of interest.
    SKlearn pipeline compatible but assumes MNE Epochs are passed in a loaded manner.
    """
    def __init__(self, filter_lower_bound=2, filter_upper_bound=32, data_tmin=0.1, data_tmax=0.6):
        """
        Please provide the:
        - filter_lower_bound: lower bound for the filter in Hz (default: 2)
        - filter_upper_bound: lower bound for the filter in Hz (default: 32)
        - data_tmin: start time of the data to be returned, in seconds from the queue onset (default 0.1)
        - data_tmax: end time of the data to be returned, in seconds from the queue onset (default 0.6)
        """
        self.filter_lower_bound = filter_lower_bound
        self.filter_upper_bound = filter_upper_bound
        self.data_tmin = data_tmin
        self.data_tmax = data_tmax

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
        # We create a copy to ensure no edit of original
        X = copy.deepcopy(X)
        
        # Perform the filter on the X
        with io.capture_output():
            X.filter(l_freq= self.filter_lower_bound,
                     h_freq= self.filter_upper_bound,
                     picks= "all",
                     phase= "minimum",
                     fir_window= "blackman",
                     fir_design= "firwin",
                     pad= 'median',
                     verbose= False)
            
            # Return the data only
            return X.get_data(tmin= self.data_tmin, tmax= self.data_tmax)
