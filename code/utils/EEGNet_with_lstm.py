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
from tensorflow.keras import regularizers
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.layers import Conv2D, AveragePooling2D
from tensorflow.keras.layers import SeparableConv2D, DepthwiseConv2D
from tensorflow.keras.layers import BatchNormalization
from tensorflow.keras.layers import SpatialDropout2D
from tensorflow.keras.layers import Input, Flatten
from tensorflow.keras.constraints import max_norm
from tensorflow.keras.layers import LSTM, Permute, Bidirectional, Lambda, Reshape, ConvLSTM1D
from tensorflow.keras import Sequential

##################################
# Custom reshape layer
##################################

def ThreeDimToTwoDimLayer(x):
    """ 
    Conversion layer needed to remove last dimension of 3D input, from (_, 25, 16, 1) -> (_, 25, 16).
    """
    
    shape = x.shape
    
    reshape = Reshape((shape[1],shape[2]*shape[3]))(x)
    
    return reshape


##################################
# EEGNET WITH BIDERECTIONAL LSTM
##################################

def EEGNet_bidirectional_lstm(nb_classes, Chans = 21, Samples = 100, 
                              dropoutRate = 0.5, kernLength = 50, F1 = 8, 
                              D = 2, F2 = 16, norm_rate = 0.3, dropoutType = 'SpatialDropout2D',
                              LSTM_size= 64, ltsm_dropout = 0.6, ltsm_l1 = 0.0001, ltsm_l2 = 0.0001):
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
      LSTM_size       : Size of LSTM layer (amount of units)
      ltsm_dropout    : Dropout after LTSM
    """
    
    if dropoutType == 'SpatialDropout2D':
        dropoutType = SpatialDropout2D
    elif dropoutType == 'Dropout':
        dropoutType = Dropout
    else:
        raise ValueError('dropoutType must be one of SpatialDropout2D '
                         'or Dropout, passed as a string.')
    
    input1   = Input(shape = (Chans, Samples, 1))

    ###################################
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
    
    model.add(AveragePooling2D((1, 2))) # Limited to maintain some form of time 
    
    model.add(dropoutType(dropoutRate))
    
    model.add(SeparableConv2D(F2, (1, 16),
                              use_bias = False, padding = 'same'))
    
    model.add(BatchNormalization())
    
    model.add(Activation('elu'))
    
    model.add(AveragePooling2D((1, 2))) # Limited to maintain some form of time 
    
    model.add(dropoutType(dropoutRate))
    
    
    ###################################
    # LSTM on found features
    
    model.add(Permute((2, 3, 1)))  # (_, 1, 25, 16) -> (_, 25, 16, 1) if 100Hz
    
    model.add(Lambda(ThreeDimToTwoDimLayer)) # (_, 25, 16, 1) -> (_, 25, 16) if 100Hz

    model.add(Bidirectional(
        LSTM(units = LSTM_size,
             activation="tanh",
             recurrent_activation="sigmoid",
             use_bias=True,
             kernel_initializer="glorot_uniform",
             recurrent_initializer="orthogonal",
             bias_initializer="zeros",
             unit_forget_bias=True,
             kernel_regularizer=regularizers.L1L2(l1= ltsm_l1, l2= ltsm_l2),
             recurrent_regularizer=None,
             kernel_constraint=None,
             recurrent_constraint=None,
             bias_constraint=None,
             dropout= ltsm_dropout,
             recurrent_dropout= 0, # Required to use the significantly faster cuDNN
             return_sequences=False,
             return_state=False,
             go_backwards=False,
             stateful=False,
             time_major=False,
             unroll=False
             )))
    
    model.add(Dropout(rate=(ltsm_dropout/2)))
    
    
    ###################################
    # CNN based "feature extraction" as per EEGNet
    
    model.add(Flatten(name = 'flatten'))
    
    # Add complixity without gain
    # model.add(Dense(128, activation='relu', name = 'dense_after_lstm'))
    
    model.add(Dense(nb_classes, name = 'dense_last', 
                    kernel_constraint = max_norm(norm_rate)))
    model.add(Activation('softmax', name = 'softmax_output'))
    
    
    return model


##################################
# EEGNET WITH LSTM 1D CONV
##################################
def EEGNet_lstm_1Dconv(nb_classes, Chans = 64, Samples = 128, 
                       dropoutRate = 0.5, kernLength = 64, F1 = 8, 
                       D = 2, norm_rate = 0.25, dropoutType = 'Dropout',
                       lstm_filters = 64, lstm_kernel_size= 4, ltsm_dropout=0.5,
                       ltsm_l1 = 0.0001, ltsm_l2 = 0.0001):
    """ 
    Extension to the Keras Implementation of EEGNet provided by ARL_EEGModels.
    Adds a Conv1D LSTM after the first block of EEGNet feature extraction as a way to provide memory to the model.

    Inputs:
      nb_classes      : int, number of classes to classify
      Chans, Samples  : number of channels and time points in the EEG data
      dropoutRate     : dropout fraction
      kernLength      : length of temporal convolution in first layer. We found
                        that setting this to be half the sampling rate worked
                        well in practice. For the SMR dataset in particular
                        since the data was high-passed at 4Hz we used a kernel
                        length of 32.     
      F1              : number of temporal filters (F1)
      D               : number of spatial filters to learn within each temporal
                        convolution. Default: D = 2
      dropoutType     : Either SpatialDropout2D or Dropout, passed as a string.
      lstm_filters    : Amount of filters for LSTM layer Conv1D. Default: 32
      lstm_kernel_size: Kernels size for LSTM layer Conv1D Default: 32
      ltsm_dropout    : Dropout after LTSM
    """
    
    if dropoutType == 'SpatialDropout2D':
        dropoutType = SpatialDropout2D
    elif dropoutType == 'Dropout':
        dropoutType = Dropout
    else:
        raise ValueError('dropoutType must be one of SpatialDropout2D '
                         'or Dropout, passed as a string.')
    
    input1   = Input(shape = (Chans, Samples, 1))

    ###################################
    # EEGNet based feature extraction
    
    block1       = Conv2D(F1, (1, kernLength), padding = 'same', # (_, 21, 100, 1) -> (_, 21, 100, 8)
                                   input_shape = (Chans, Samples, 1), 
                                   use_bias = False)(input1)
    block1       = BatchNormalization()(block1)
    block1       = DepthwiseConv2D((Chans, 1), use_bias = False, # (_, 21, 100, 8) -> (_, 1, 100, 16)
                                   depth_multiplier = D,
                                   depthwise_constraint = max_norm(1.))(block1)
    block1       = BatchNormalization()(block1)
    block1       = Activation('elu')(block1)
    block1       = dropoutType(dropoutRate)(block1)
    
    ###################################
    # LSTM CONV LAYER
    
    reshape      = Permute((2, 1, 3))(block1) # (_, 1, 100, 16) -> (None, 100, 1, 16)
    
    lstmconv     = Bidirectional(ConvLSTM1D(filters = lstm_filters,
                                            kernel_size = lstm_kernel_size,
                                            strides= 1,
                                            padding= "valid", # reduces dimension
                                            kernel_regularizer=regularizers.L1L2(l1= ltsm_l1, l2= ltsm_l2),
                                            data_format= "channels_first", # 21 electrodes
                                            stateful= False,
                                            dropout= ltsm_dropout,
                                            recurrent_dropout= 0))(reshape) # For speed
    
    lstmdrop     = Dropout(rate=(ltsm_dropout/2))(lstmconv)

       
    ###################################
    # EEGNET BASED CLASSIFICATION
     
    flatten      = Flatten(name = 'flatten')(lstmdrop)
    
    # Increases complexity without gain
    #bigdense     = Dense(128, activation='relu', name = 'dense_after_lstm')(flatten)
    
    dense        = Dense(nb_classes, name = 'dense', 
                         kernel_constraint = max_norm(norm_rate))(flatten)
    softmax      = Activation('softmax', name = 'softmax')(dense)
    
    return Model(inputs=input1, outputs=softmax)