# BCI Master Thesis @ VUB 2021 - 2022

This repository includes installation instructions, source code, extra documents and more from Lennert Bontinck's Master Thesis @ VUB 2021 - 2022.

The current draft version of the thesis can be found [here](paper/bci_master_thesis.pdf), the source code of this LaTeX document is [also available](paper/source).

## Table of contents

- [Contact information](#contact-information)
- [Documentation](#documentation)
  - [Installation instructions](#installation-instructions)
  - [Initialisation instructions](#initialisation-instructions)
- [Code](#code)
  - [Utils](#utils)
  - [Experimental notebooks](#experimental-notebooks)
- [Literature review](#literature-review)
  - [Scientific sources](#scientific-sources)
  - [Informal sources](#informal-sources)

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

Most of the libraries related to the OpenBCI hardware works best on Windows machines. Some of the required dependencies aren't even available on macOS, for this reason these install instructions focus mainly on Windows 10 machines. However, a conda environment for macOS is also made available as well as some notes for macOS specific installs. Non OpenBCI related code works well on both macOS and Windows normally, although Windows is still adviced.

| Title                                        | Documentation                                          |
| -------------------------------------------- | ------------------------------------------------------ |
| Install instructions of anaconda environment | Available [here](documentation/installation/README.md) |



### Initialisation instructions

Running the anaconda environment to open the Jupyter Notebooks is straightforward when the environment is installed as discussed above. For completeness some instructions on running the environment are given as well.

| Title                                      | Documentation                                            |
| ------------------------------------------ | -------------------------------------------------------- |
| Initialisation of the Anaconda environment | Available [here](documentation/initialisation/README.md) |

<hr>


## Code

To make reproducing the project easier, all of the code used is provided.

### Utils

Some util files are provided to extract certain aspects from the main notebooks such as data retrieval.

| Title            | Location                                    |
| ---------------- | ------------------------------------------- |
| CLA dataset util | Available [here](code/utils/CLA_dataset.py) |



### Experimental notebooks

Some of the code written is not used explicitly in the paper but was used to gain information or test code that will be used in the final project. We call these experimental notebooks. The following experimental notebooks are available:

| Title                                                        | Location                                                     |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| 1: CLA dataset exploration notebook                          | Available [here](code/experimental-notebooks/1-CLA-dataset-exploration-notebook.ipynb) |
| 2: MNE datastructure exploration notebook                    | Available [here](code/experimental-notebooks/2-MNE-datastructure-exploration-notebook.ipynb) |
| 3: MNE epoching                                              | Available [here](code/experimental-notebooks/3-MNE-epoching.ipynb) |
| 4: CSP based classification                                  | Available [here](code/experimental-notebooks/4-CSP-based-classification.ipynb) |
| 5: CSP based classification using parameters from the previous subject | Available [here](code/experimental-notebooks/5-CSP-params-new-subject.ipynb) |
| 6: Deep Learning based classification                        | Available [here](code/experimental-notebooks/6-DL-based-classification.ipynb) |
| 7: Improving inter-session EEGNet                            | Available [here](code/experimental-notebooks/7-improving-inter-session-eegnet.ipynb) |




<hr>


## Literature review

The literature review is one of the most important aspects of any scientific paper. All scientific sources that were consulted are available in a Zotero maintained list.


### Scientific sources

As this master thesis should be scientific grade, the sources should also be scientific. Finding good sources isn't an easy task since there are so many to choose from. Luckily Arnau Dillen and Geraint Wiggins gave some great pointers on where to begin and how to proceed. A list of all scientific sources is available in the form of a Zotero file, more information on the scientific literature used for the thesis [is available here](literature-review/zotero/README.md).

### Informal sources

There are a lot of interesting YouTube videos, blog posts and more about the thesis topic that were also consulted. They are insightful to understand how the different aspects work in real life. However, these sources are not peer-reviewed and thus don't have much scientific value. The table below gives an overview of the most interesting ones.

| Title                                   | Type                                                         | Notes                                                        |
| --------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Testing Brain-Computer Interfaces       | Youtube video by [James Bruton - 1M subs](https://www.youtube.com/channel/UCUbDcUPed50Y_7KmfCXKohA) | Notes available [here](literature-review/informal/youtube/james_bruton-testing_BCIs.md) |
| NeuroTechX Webinars (1-3)               | Professional webinars by [NeuroTechX](https://neurotechx.com/) | Notes available [here](literature-review/informal/NeuroTechX-webinar/notes.md) |
| Pybrain: M/EEG analysis with MNE Python | Workshop by Richard Höchenberger - 8 hours                   | References throughout multiple notebooks                     |


* * *
* * *
##### © [Lennert Bontinck](https://www.lennertbontinck.com/) VUB 2021-2022