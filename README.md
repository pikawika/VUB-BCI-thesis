# BCI Master Thesis @ VUB 2021 - 2022

This repository includes installation instructions, source code, extra documents and more from Lennert Bontinck's Master Thesis on processing and using EEG signals from motor imagery tasks in a BCI setting @ VUB 2021 - 2022.

The current draft version of the thesis can be found [here](paper/bci_master_thesis.pdf), the source code of this LaTeX document is [also available](paper/source) and the source files for the figures are available [here](figures/).

## Table of contents

- [BCI Master Thesis @ VUB 2021 - 2022](#bci-master-thesis--vub-2021---2022)
  - [Table of contents](#table-of-contents)
  - [Contact information](#contact-information)
  - [Documentation](#documentation)
    - [Installation instructions](#installation-instructions)
    - [Initialisation instructions](#initialisation-instructions)
  - [Code](#code)
    - [Utility files](#utility-files)
    - [Experimental notebooks](#experimental-notebooks)
    - [Paper notebooks](#paper-notebooks)
  - [Literature review](#literature-review)
    - [Scientific sources](#scientific-sources)
    - [Informal sources](#informal-sources)
        - [© Lennert Bontinck VUB 2021-2022](#-lennert-bontinck-vub-2021-2022)

<hr>


## Contact information

| Name             | Role                 | VUB mail                                                  | Personal mail                                               |
| ---------------- | -------------------- | --------------------------------------------------------- | ----------------------------------------------------------- |
| Lennert Bontinck | Master Thesis writer | [lennert.bontinck@vub.be](mailto:lennert.bontinck@vub.be) | [info@lennertbontinck.com](mailto:info@lennertbontinck.com) |
| Geraint Wiggins  | Promotor             | [geraint.wiggins@vub.be](mailto:geraint.wiggins@vub.be)   | /                                                           |
| Arnau Dillen     | Supervisor           | [arnau.dillen@vub.be](mailto:arnau.dillen@vub.be)         | /                                                           |
| Kevin De Pauw    | Co-Supervisor        | [kevin.de.pauw@vub.be](mailto:kevin.de.pauw@vub.be)       | /                                                           |

<hr>


## Documentation

To make reproducing the project easier, the following documentation is provided.

### Installation instructions

Most of the libraries related to the OpenBCI hardware work best on Windows machines. Some of the required dependencies aren't even available on macOS, for this reason, these install instructions focus mainly on Windows 10 machines. However, a conda environment for macOS is also made available as well as some notes for macOS-specific installs. Non-OpenBCI-related code works well on both macOS and Windows normally, although Windows is still advised.

| Title                                        | Documentation                                          |
| -------------------------------------------- | ------------------------------------------------------ |
| Install instructions of anaconda environment | Available [here](documentation/installation/README.md) |



### Initialisation instructions

Running the anaconda environment to open the Jupyter Notebooks is straightforward when the environment is installed as discussed above. For completeness, some instructions on running the environment are given as well.

| Title                                      | Documentation                                            |
| ------------------------------------------ | -------------------------------------------------------- |
| Initialisation of the Anaconda environment | Available [here](documentation/initialisation/README.md) |

<hr>


## Code

All of the code used for creating the paper associated with this thesis and more are provided to ensure full transparency.

### Utility files

Some utility files are provided to extract certain aspects from the main notebooks such as data retrieval in a simply python importable utility file. Import instructions for the utility files are given in the header of the corresponding file. 

| Title            | Location                                    |
| ---------------- | ------------------------------------------- |
| CLA dataset util | Available [here](code/utils/CLA_dataset.py) |
| TF tools         | Available [here](code/utils/TF_tools.py)    |
| EEG models       | Available [here](code/utils/EEGModels.py)   |



### Experimental notebooks

Some of the code written is not used explicitly in the paper but was used to gain information or test code that will be used in the final project. We call these experimental notebooks and they contain a lot of annotations as well. The following experimental notebooks are available:

| Title                                                        | Notebook location                                            |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| 1: CLA dataset exploration notebook                          | Available [here](code/experimental-notebooks/1-CLA-dataset-exploration-notebook.ipynb) |
| 2: MNE datastructure exploration notebook                    | Available [here](code/experimental-notebooks/2-MNE-datastructure-exploration-notebook.ipynb) |
| 3: MNE epoching                                              | Available [here](code/experimental-notebooks/3-MNE-epoching.ipynb) |
| 4: CSP based classification                                  | Available [here](code/experimental-notebooks/4-CSP-based-classification.ipynb) |
| 5: CSP based classification using parameters from the previous subject | Available [here](code/experimental-notebooks/5-CSP-params-new-subject.ipynb) |
| 6: Deep Learning based classification                        | Available [here](code/experimental-notebooks/6-DL-based-classification.ipynb) |
| 7: Improving inter-session EEGNet                            | Available [here](code/experimental-notebooks/7-improving-inter-session-eegnet.ipynb) |



### Paper notebooks

What we refer to as paper notebooks are notebooks which include code for experiments and plotting results that are directly used in the paper or directly referenced in the paper. Special attention to reproduction and well-documented code is given in these notebooks to improve their scientific value. A HTML export of each notebook is made so the code and output can be looked at without requiring the Anaconda environment.

| Title      | Notebook location                              | HTML export location |
| ---------- | ------------------------------------------------------ | ---------- |
| 1: Data visualisation | Available [here](code/paper-notebooks/1-data-visualisation.ipynb) |  |
| 2: Standard CSP pipelines | Available [here](code/paper-notebooks/2-standard-csp-pipelines.ipynb) | Available [here](code/paper-notebooks/HTML_exports/2-standard-csp-pipelines.html) |
| 3: Advanced CSP pipelines |  |  |
| 4: EEGNet | Available [here](code/paper-notebooks/4-eegnet.ipynb) | Available [here](code/paper-notebooks/HTML_exports/4-eegnet.html) |
| 5: DeepConvNet            | Available [here](code/paper-notebooks/5-deepconvnet.ipynb) | Available [here](code/paper-notebooks/HTML_exports/5-deepconvnet.html) |
| 6: ShallowConvNet | Available [here](code/paper-notebooks/6-shallowconvnet.ipynb) | |
| 7: Extensions |  | |
| 8: Going online |  | |
| A: Figures | Available [here](code/paper-notebooks/A-figures.ipynb) | |


****


<hr>


## Literature review

The literature review is one of the most important aspects of any scientific paper. All scientific sources that were considered are available in a Zotero maintained list, the reference list of the paper lists all of these sources that are effectively used in the paper, both directly as indirectly.


### Scientific sources

As this master thesis should be scientific grade, the sources should also be scientific. Finding good sources isn't an easy task since there are so many to choose from. Luckily Arnau Dillen and Geraint Wiggins gave some great pointers on where to begin and how to proceed. A list of all scientific sources is available in the form of a Zotero file, more information on the scientific literature used for the thesis [is available here](literature-review/zotero/README.md).

### Informal sources

For more intuitive insight into certain aspects of both code and theory, some informal sources were also used. The most important ones are listed below and are summarized to inform what was intuitively gained from them.

| Title                                   | Type                                                         | Notes                                                        |
| --------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Testing Brain-Computer Interfaces       | Youtube video by [James Bruton - 1M subs](https://www.youtube.com/channel/UCUbDcUPed50Y_7KmfCXKohA) | Notes available [here](literature-review/informal/youtube/james_bruton-testing_BCIs.md) |
| NeuroTechX Webinars (1-3)               | Professional webinars by [NeuroTechX](https://neurotechx.com/) | Notes available [here](literature-review/informal/NeuroTechX-webinar/notes.md) |
| Pybrain: M/EEG analysis with MNE Python | Workshop by Richard Höchenberger - 8 hours                   | References throughout multiple notebooks                     |


* * *
* * *
##### © [Lennert Bontinck](https://www.lennertbontinck.com/) VUB 2021-2022