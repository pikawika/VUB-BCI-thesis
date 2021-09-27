# Install instructions for macOS (NOT RECOMMENDED)

OpenBCI hardware and software works best on Windows. Some software, such as OpenViBE, doesn't even support macOS. The use of a Windows machine or VM is thus recommended. The software for this master thesis was mainly developed on a Windows 10 machine. These macOS instructions may thus not be complete enough to run the master thesis project as macOS was not used for the development.

## Table of contents

[[_TOC_]]



## Author

| Name             | Role                 | VUB mail                                                  | Personal mail                                               |
| ---------------- | -------------------- | --------------------------------------------------------- | ----------------------------------------------------------- |
| Lennert Bontinck | Master Thesis writer | [lennert.bontinck@vub.be](mailto:lennert.bontinck@vub.be) | [info@lennertbontinck.com](mailto:info@lennertbontinck.com) |



## OpenBCI GUI

Installing OpenBCI GUI should be straightforward and the steps can be followed from [the online doc](https://openbci.com/downloads). However, some important macOS related notes have to be made:

- Install `CYTON DONGLE DRIVERS`from the OpenBCI website or from [the FTDI Chip website](https://ftdichip.com/drivers/vcp-drivers/).
  - **WARNING**: place the installer in the `/application` folder before opening it. The macOS installer is in Beta as of September 2021 and requires this hack to work correctly.
- Instal `OpenBCI GUI`.
  - **WARNING**: V5.0.6, which was the latest version as of September 2021, has a bug on macOS where only a white screen is shown. Using the older V5.0.5 should work. This older version can be found under [the GitHub releases](https://github.com/OpenBCI/OpenBCI_GUI/releases).



## Setting up Anaconda environment

The instructions below highlight the steps needed to recreate the used anaconda environment.

### Configuring the base environment

- Install [the free version of Anaconda Navigator](https://www.anaconda.com/products/individual).

- From the Anaconda Navigator GUI, create a new environment named `bci-master-thesis`.

  - Include both Python and R. The following versions were used:
    - `Python 3.8.11`
    -  `R 3.6.1`
  - Doing so should install a whole suite of packages by default 

- The following packages need to be installed additionally

  - `pandas` (and its dependencies)
  - `pyqtgraph` (and dependencies)
  - `matplotlib` (and dependencies)

- Using your terminal, activate the newly created environment

  - ```shell
    # Activates the previously created bci-master-thesis Anaconda environment.
    conda activate bci-master-thesis
    ```

- Install some conda available packages on the environment

  - ```shell
    # Pandas is a famous Python Data Analysis Library and is used by a lot of other packages.
    # The following command installs Pandas and its dependencies. V1.3.2 was used.
    conda install pandas
    # We install pip to install packages not available from conda install. V21.2.2 was used.
    conda install pip
    ```
  
- Install some pip available packages on the environment

  - ```shell
    # MNE is a famous Python package for visualising and working with neurophysiological data.
    # V0.23.4 was used.
    pip install mne
    ```

- Try [code samples from brainflow](https://brainflow.readthedocs.io/en/stable/Examples.html#python)

  - Or see seperate [notebook containing initial tries](../../sample_code/first_attempts.ipynb).

### Installing BrainFlow for Python connection

Whilst [OpenBCI LSL for Python connection](https://docs.openbci.com/Software/CompatibleThirdPartySoftware/LSL/) will be used for the master thesis project, BrainFlow is also a great option for quickly connecting your OpenBCI with Python. Details on BrainFlow are available [here](https://docs.openbci.com/ForDevelopers/SoftwareDevelopment/).

- Using your terminal, activate the previously created environment

  - ```shell
    # Activates the previously created bci-master-thesis Anaconda environment
    conda activate bci-master-thesis
    ```

- Install BrainFlow via pip

  - ```shell
    # BrainFlow is a library intended to obtain, parse and analyze EEG, EMG, ECG and other kinds of data from biosensors such as the ones on OpenBCI.
    # V4.6.1 was used.
    pip install brainflow
    ```

### Configuring the environment from the YML file

The anaconda macOS environment is also exported to the `bci-master-thesis-environment-mac.yml` YML file. This file is available [here](environments/bci-master-thesis-environment-mac.yml). You can load it in via the terminal as follows:


```shell
# Navigate to the folder where the YML file is located
cd bci-master-thesis/documentation/installation/environments
# Configure a new environment from the YML file
conda env create -f bci-master-thesis-environment-mac.yml
```