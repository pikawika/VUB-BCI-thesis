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
- [Side information](#side-information)
  - [Promosing software and datasets](#promosing-software-and-datasets)
  - [Drafts](#drafts)

<hr>


## Contact information

| Name             | Role                 | VUB mail                                                  | Personal mail                                               |
| ---------------- | -------------------- | --------------------------------------------------------- | ----------------------------------------------------------- |
| Lennert Bontinck | Master Thesis writer | [lennert.bontinck@vub.be](mailto:lennert.bontinck@vub.be) | [info@lennertbontinck.com](mailto:info@lennertbontinck.com) |
| Arnau Dillen     | Supervisor           | [arnau.dillen@vub.be](mailto:arnau.dillen@vub.be)         | /                                                           |
| Geraint Wiggins  | Promotor             | [geraint.wiggins@vub.be](mailto:geraint.wiggins@vub.be)   | /                                                           |
| Kevin De Pauw    | Co-Supervisor        | [kevin.de.pauw@vub.be](mailto:kevin.de.pauw@vub.be)       | /                                                           |

<hr>


## Documentation

To make reproducing the project easier, the following documentation is provided.

### Installation instructions

OpenBCI hardware and software works best on Windows. Some software, such as OpenViBE, doesn't even support macOS. The use of a Windows machine or VM is thus recommended. The software for this master thesis was mainly developed on a Windows 10 machine. Reproducibility on other operating systems can't be guaranteed.

| Title                                            | Documentation                                           |
| ------------------------------------------------ | ------------------------------------------------------- |
| Install instructions for Windows (RECOMMENDED)   | Available [here](documentation/installation/windows.md) |
| Install instructions for macOS (NOT RECOMMENDED) | Available [here](documentation/installation/macos.md)   |



### Initialisation instructions

| Title                                      | Documentation                                                |
| ------------------------------------------ | ------------------------------------------------------------ |
| Initialisation of the Anaconda environment | Available [here](documentation/initialisation/initialisation-instructions.md) |

<hr>


## Code

To make reproducing the project easier, all of the code used is provided.

### Utils

Some util files are provided to extract certain aspects from the main notebooks such as data retrieval.

| Title            | Location                                    |
| ---------------- | ------------------------------------------- |
| CLA dataset util | Available [here](code/utils/CLA_dataset.py) |



### Experimental notebooks

Some of the code written is not used explicitly in the paper but was used to gain information. We call these experimental notebooks. The following experimental notebooks are available:

| Title                                   | Location                                                     |
| --------------------------------------- | ------------------------------------------------------------ |
| CLA dataset exploration notebook        | Available [here](code/experimental-notebooks/CLA-dataset-exploration-notebook.ipynb) |
| MNE data structure exploration notebook | Available [here](code/experimental-notebooks/MNE-datastructure-exploration-notebook.ipynb) |


<hr>


## Literature review

The literature review is one of the most important aspects of any scientific paper. To better understand the complex topic of BCIs, both scientific papers and more informal sources were consulted. In the table below some of these sources and their synthesis are given. A list of all sources used for the master thesis is available through the literature tools, more on this [here](side-information/software/literature_tools.md).


### Scientific sources

As this master thesis should be scientific grade, the sources should also be scientific. Finding good sources isn't an easy task since there are so many to choose from. Luckily Arnau Dillen and Geraint Wiggins gave some great pointers on where to begin and how to proceed. Per the recommendation of Geraint Wiggins, an overview sheet of all these sources was made. The table below gives an overview of the most interesting scientific sources and the notes made for them.

| Title                                                        | Type                                                         | Notes                                                        |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Overview sheet for all scientific sources                    | Simple overview sheet                                        | Excel available [here](literature-review/scientific/overview/overview_sheet.xlsx) |
| EEGPLUS: Making a Hybrid Brain Computer Interface Using EEG and EMG Signals | Master thesis by [Arnau Dillen](https://researchportal.vub.be/en/studentTheses/eegplus-making-a-hybrid-brain-computer-interface-using-eeg-and-em) | Annotated pdf available on [Zotero](side-information/software/literature_tools.md#zotero) |
| NeuroTechX Webinars (1-9)                                    | Professional webinars by [NeuroTechX](https://neurotechx.com/) | Notes available [here](literature-review/scientific/NeuroTechX-webinar/notes.md) |



### Informal sources

There are a lot of interesting YouTube videos, blog posts and more about the thesis topic, especially about OpenBCI. They are insightful to understand how the different aspects work in real life. However, these sources are not peer-reviewed and thus don't have much scientific value. The table below gives an overview of the most interesting ones and the notes made for them.

| Title                             | Type                                                         | Notes                                                        |
| --------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Testing Brain-Computer Interfaces | Youtube video by [James Bruton - 1M subs](https://www.youtube.com/channel/UCUbDcUPed50Y_7KmfCXKohA) | Notes available [here](literature-review/informal/youtube/james_bruton-testing_BCIs.md) |

<hr>


## Side information

To ensure full transparency and reproducibility, all of the other documents made for the project are provided here. These include meeting summaries, brainstorm sheets and more. 

### Promosing software and datasets

Some promising software and datasets were found along the way when researching the topic. They might be helpful for the project.

| Title                      | Documentation                                                |
| -------------------------- | ------------------------------------------------------------ |
| Promising Python Libraries | Available [here](side-information/software/python_libraries.md) |
| Literature tools           | Available [here](side-information/software/literature_tools.md) |
| Interesting datasets       | Available [here](side-information/datasets/interesting_datasets.md) |



### Drafts

| Title                  | Document                                                  |
| ---------------------- | --------------------------------------------------------- |
| Draft for ideas        | Available [here](side-information/brainstorming/ideas.md) |
| Draft for things to do | Available [here](side-information/brainstorming/todo.md)  |


* * *
* * *
© [Lennert Bontinck](https://www.lennertbontinck.com/) VUB 2021-2022