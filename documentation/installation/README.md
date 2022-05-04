# Install instructions of anaconda environment

Most of the libraries related to the OpenBCI hardware works best on Windows machines. Some of the required dependencies aren't even available on macOS, for this reason these install instructions focus mainly on Windows 10 machines. However, a conda environment for macOS is also made available as well as some notes for macOS specific installs.

## Table of contents

- [Author](#author)
- [OpenBCI GUI](#openbci-gui)
- [MacOS specific preruiqisite](#macos-specific-preruiqisite)
- [Setting up Anaconda environment](#setting-up-anaconda-environment)
  * [Configuring the base environment](#configuring-the-base-environment)
  * [Configuring the environment from the YML file](#configuring-the-environment-from-the-yml-file)

<hr>


## Author

| Name             | Role                 | VUB mail                                                  | Personal mail                                               |
| ---------------- | -------------------- | --------------------------------------------------------- | ----------------------------------------------------------- |
| Lennert Bontinck | Master Thesis writer | [lennert.bontinck@vub.be](mailto:lennert.bontinck@vub.be) | [info@lennertbontinck.com](mailto:info@lennertbontinck.com) |

<hr>


## OpenBCI GUI

Installing OpenBCI GUI should be straightforward and the steps can be followed from [the online doc](https://openbci.com/downloads).

- Install `CYTON DONGLE DRIVERS`from the OpenBCI website or from [the FTDI Chip website](https://ftdichip.com/drivers/vcp-drivers/). The FTDI chip website has an easy  `setup executable`.
  - Version 2.12.36.4 was used.
  - MacOS note: place the installer in the `/application` folder before opening it. The macOS installer is in Beta as of September 2021 and requires this hack to work correctly.
- Instal `OpenBCI GUI`.
  - Version 5.0.8 was used.
  - MacOS note: V5.0.6, which was the latest version as of September 2021, has a bug on macOS where only a white screen is shown. Using the older V5.0.5 should work. This older version can be found under [the GitHub releases](https://github.com/OpenBCI/OpenBCI_GUI/releases).

<hr>


## MacOS specific preruiqisite

To use the  `PyQt5`  backend for Matplotlib, which is recommended for MNE plotting, `pyqt` needs to be installed via Homebrew.

```shell
brew install pyqt
```

<hr>

## Setting up Anaconda environment


The instructions below highlight the steps needed to recreate the used anaconda environment.

### Configuring the base environment

- Install [the free version of Anaconda Navigator](https://www.anaconda.com/products/individual). V2.1.4 was used.

- From the Anaconda Navigator GUI, create a new environment named `bci-master-thesis`.

  - Include both Python and R. The following versions were used:
    - `Python 3.8.10`
    -  `R 3.6.1`
  - Doing so should install a whole suite of packages by default 

- Using the `Anaconda Prompt (Anaconda3)` application, activate the newly created environment.

  - **NOTE**: it might be required to run the prompt as administrator for all of the below steps.

  - ```shell
    # Activates the previously created bci-master-thesis Anaconda environment.
    conda activate bci-master-thesis
    ```

- Install some conda available packages on the environment

  - ```shell
    # Pandas is a famous Python Data Analysis Library and is used by a lot of other packages.
    # The following command installs Pandas and its dependencies. V1.4.1 was used.
    conda install pandas
    
    # We install pip to install packages not available from conda install. V21.2.2 was used.
    conda install pip
    ```
  
- Install some pip available packages on the environment

  - ```shell
    # MNE is a famous Python package for visualising and working with neurophysiological data.
    # V1.0.2 was used.
    pip install mne
    
    # Install Matplotlib for plotting purposes.
    # V3.5.1 was used.
    pip install matplotlib
    
    # Install backend for matplotlib visualisations.
    # V5.15.6 was used.
    pip install PyQt5
    
    # Install Sci-Kit learn for ML.
    # V1.0.2 was used.
    pip install -U scikit-learn
    
    # Install LightGBM for ML.
    # V3.3.2 was used.
    pip install lightgbm
    ```



### Configuring the environment from the YML file

The anaconda Windows environment is also exported to the `bci-master-thesis-environment-windows.yml` YML file. This file is available [here](environments/bci-master-thesis-environment-windows.yml). You can load it in via the terminal as follows:


```shell
# Navigate to the folder where the YML file is located
cd bci-master-thesis/documentation/installation/environments
# Configure a new environment from the YML file
# These were exported using: conda env export > file.yml --no-builds
## Note: macOS variant of file available
conda env create -f bci-master-thesis-environment-windows.yml
```

* * *
* * *
© [Lennert Bontinck](https://www.lennertbontinck.com/) VUB 2021-2022