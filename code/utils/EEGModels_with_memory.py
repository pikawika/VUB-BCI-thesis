# This util provides an extension of EEG-related TF models from literature to provide some form of memory.
# These models are modified from work provided by
#   ARL_EEGModels - A collection of Convolutional Neural Network models for EEG
#   https://github.com/vlawhern/arl-eegmodels

# Import it as follows:
# | import sys
# | sys.path.append('../utils')
# | import EEGModels_with_memory

##################################
# IMPORTS
##################################

from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.layers import Conv2D, AveragePooling2D
from tensorflow.keras.layers import SeparableConv2D, DepthwiseConv2D
from tensorflow.keras.layers import BatchNormalization
from tensorflow.keras.layers import SpatialDropout2D
from tensorflow.keras.layers import Input, Flatten
from tensorflow.keras.constraints import max_norm
from tensorflow.keras.layers import LSTM, TimeDistributed, Bidirectional, Lambda, Reshape
from tensorflow.keras import Sequential

##################################
# Custom reshape layer
##################################

def ThreeDimToTwoDimLayer(x):
    
    shape = x.shape
    
    # 1 possibility: H,W*channel
    reshape = Reshape((shape[1],shape[2]*shape[3]))(x)
    
    # 2 possibility: W,H*channel
    # transpose = Permute((2,1,3))(x)
    # reshape = Reshape((shape[1],shape[2]*shape[3]))(transpose)
    
    return reshape

def EEGNet_bidirectional_lstm(nb_classes, Chans = 64, Samples = 128, 
                              dropoutRate = 0.5, kernLength = 64, F1 = 8, 
                              D = 2, F2 = 16, norm_rate = 0.25, dropoutType = 'Dropout',
                              LSTM_size= 4):
    """ 
    Extension to the Keras Implementation of EEGNet provided by ARL_EEGModels.
    Adds a singular biderectional LSTM after the EEGNet feature extraction as a way to provide memory to the model.

    Inputs:
      nb_classes      : int, number of classes to classify
      Chans, Samples  : number of channels and time points in the EEG data
      dropoutRate     : dropout fraction
      kernLength      : length of temporal convolution in first layer. We found
                        that setting this to be half the sampling rate worked
                        well in practice. For the SMR dataset in particular
                        since the data was high-passed at 4Hz we used a kernel
                        length of 32.     
      F1, F2          : number of temporal filters (F1) and number of pointwise
                        filters (F2) to learn. Default: F1 = 8, F2 = F1 * D. 
      D               : number of spatial filters to learn within each temporal
                        convolution. Default: D = 2
      dropoutType     : Either SpatialDropout2D or Dropout, passed as a string.
      LSTM_size       : Size 
    """
    
    if dropoutType == 'SpatialDropout2D':
        dropoutType = SpatialDropout2D
    elif dropoutType == 'Dropout':
        dropoutType = Dropout
    else:
        raise ValueError('dropoutType must be one of SpatialDropout2D '
                         'or Dropout, passed as a string.')
    
    input1   = Input(shape = (Chans, Samples, 1))

    ##################################################################
    # CNN based "feature extraction" as per EEGNet
    model = Sequential()
    model.add(Conv2D(F1, (1, kernLength), padding = 'same',
                     input_shape = (Chans, Samples, 1),
                     use_bias = False))
    
    model.add(BatchNormalization())
    
    model.add(DepthwiseConv2D((Chans, 1), use_bias = False, 
                              depth_multiplier = D,
                              depthwise_constraint = max_norm(1.)))
    
    model.add(BatchNormalization())
    
    model.add(Activation('elu'))
    
    model.add(AveragePooling2D((1, 4)))
    
    model.add(dropoutType(dropoutRate))
    
    model.add(SeparableConv2D(F2, (1, 16),
                              use_bias = False, padding = 'same'))
    
    model.add(BatchNormalization())
    
    model.add(Activation('elu'))
    
    model.add(AveragePooling2D((1, 8)))
    
    model.add(dropoutType(dropoutRate))
    
    
    ##################################################################
    # LTSM on found features
    
    model.add(Lambda(ThreeDimToTwoDimLayer)) # <========== pass from 4D to 3D


    model.add(Bidirectional(LSTM(LSTM_size)))
    
    
    ##################################################################
    # CNN based "feature extraction" as per EEGNet
    
    model.add(Flatten(name = 'flatten'))
    model.add(Dense(nb_classes, name = 'dense', 
                    kernel_constraint = max_norm(norm_rate)))
    model.add(Activation('softmax', name = 'softmax'))
    
    
    return model

