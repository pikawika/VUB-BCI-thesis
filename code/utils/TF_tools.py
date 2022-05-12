# This util provides some TensorFlow (TF) specific helper functions.

# Import it as follows:
# | import sys
# | sys.path.append('../utils')
# | import TF_tools

##################################
# IMPORTS
##################################

# TensorFlow
import tensorflow as tf # V2.8.0 recommended
import keras # V2.8.0 recommended

##################################
# FUNCTIONS
##################################


def check_tf_cpu_gpu_presence():
    """Checks what CPUs and GPUs are present for use in TensorFlow."""
    # Example call: TF_tools.check_tf_cpu_gpu_presence()
    
    nr_cpus = len(tf.config.list_physical_devices('CPU'))
    nr_gpus = len(tf.config.list_physical_devices('GPU'))
    
    if ((nr_cpus) < 1):
        print("There are not CPUs available.")
    else:
        print(f"There are {nr_cpus} CPUs available under the names:")
        print(tf.config.list_physical_devices('CPU'))
        
    print("\n")
    
    if ((nr_gpus) < 1):
        print("There are not GPUs available.")
    else:
        print(f"There are {nr_gpus} GPUs available under the names:")
        print(tf.config.list_physical_devices('GPU'))
        
def tensorboard_callback(log_name: str, log_dir= "./logs/", update_freq = "batch"):
    """
    Returns a callback that allows for saving logs with the specified name for TensorBoard.
    Uses ./logs/ dir per default and update frequency of batch.
    """
    return tf.keras.callbacks.TensorBoard(log_dir + log_name,
                                          update_freq= update_freq,
                                          profile_batch=0)
        
def lowest_loss_model_save_callback(filepath: str):
    """
    Returns a callback that allows for saving the best model based on lowest loss for the validation set.
    Suffixes provided path with '_lowest_loss_model.hdf5'
    """
    filepath = filepath + "_lowest_loss_model.hdf5"
    return keras.callbacks.ModelCheckpoint(filepath=filepath,
                                           monitor= 'val_loss',
                                           verbose=1,
                                           save_best_only=True,
                                           mode= 'min')
    
def load_lowest_loss_model(filepath: str, custom_objects = {}):
    """
    Loads a previously stored lowest loss model.
    Suffixes provided path with '_lowest_loss_model.hdf5'.
    For custom models, it might be needed to supply extra custom objects.
    """
    filepath = filepath + "_lowest_loss_model.hdf5"
    return keras.models.load_model(filepath, custom_objects=custom_objects)

def highest_accuracy_model_save_callback(filepath: str):
    """
    Returns a callback that allows for saving the best model based on highest accuracy for the validation set.
    Suffixes provided path with '_highest_acc_model.hdf5'
    """
    filepath = filepath + "_highest_acc_model.hdf5"
    return keras.callbacks.ModelCheckpoint(filepath=filepath,
                                           monitor= 'val_accuracy',
                                           verbose=1, 
                                           save_best_only=True,
                                           mode= 'max')
    
def load_highest_accuracy_model(filepath: str, custom_objects = {}):
    """
    Loads a previously stored highest accuracy model.
    Suffixes provided path with '_highest_acc_model.hdf5'.
    For custom models, it might be needed to supply extra custom objects.
    """
    filepath = filepath + "_highest_acc_model.hdf5"
    return keras.models.load_model(filepath, custom_objects=custom_objects)