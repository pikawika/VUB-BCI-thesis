# Interesting datasets

This file contains some interesting datasets that might be useful for the project.

## Table of contents

- [Author](#author)
- [Datasets](#datasets)
  * [Multiple datasets available on one GitHub repository](#multiple-datasets-available-on-one-github-repository)
<hr>


## Author

| Name             | Role                 | VUB mail                                                  | Personal mail                                               |
| ---------------- | -------------------- | --------------------------------------------------------- | ----------------------------------------------------------- |
| Lennert Bontinck | Master Thesis writer | [lennert.bontinck@vub.be](mailto:lennert.bontinck@vub.be) | [info@lennertbontinck.com](mailto:info@lennertbontinck.com) |

<hr>


## Datasets

### Multiple datasets available on one GitHub repository

[This GitHub repository](https://github.com/meagmohit/EEG-Datasets) has multiple publicly available EEG-Datasets. It was recommended by Arnau.

### A large electroencephalographic motor imagery dataset for electroencephalographic brain computer interfaces

The DOI of the paper is available [here](https://doi.org/10.1038/sdata.2018.211). The dataset is available [here](https://doi.org/10.6084/m9.figshare.c.3917698.v1). Some notes on the dataset are given below:

- Retreived from the overview GitHub repository above.
- The dataset contains 60 hours of EEG BCI recordings spread across 75 experiments and 13 participants, featuring 60,000 mental imagery examples in 4 different BCI interaction paradigms with up to 6 EEG BCI interaction states.
  - 4.8 hours of EEG recordings and 4600 mental imagery examples are available per participant, on average, with good longitudinal and lateral dataset span as well as significant EEG BCI interaction complexity. 
- EEG data were acquired using an EEG-1200 JE-921A EEG system (medical EEG).
- 19 EEG input leads in the standard 10/20 international system have been used.
- The preparations took about 30 min per recording session.
- No electromagnetic shielding or artifact control was attempted for the recordings.
- A band-pass filter of 0.53-70 Hz was present in all EEG data recorded at 200 Hz sampling rate in the Neurofax software. A 0.53–100 Hz band-pass filter (the widest choice possible in Neurofax software) was applied to the EEG recordings acquired at 1000 Hz sampling rate.
- A 50 Hz notch filter is present in the EEG-1200 hardware to reduce electrical grid interference.
- Synchronisation is difficult as clocks in machines differ and even slight disreptencies add up over time.
- All data in this dataset were recorded in a synchronous BCI paradigm. Each experimental BCI segment consisted of a series of BCI interaction trials in which a visual action signal was shown on the computer screen instructing the participants to implement a given mental image.
  - The action signal remained on the screen for 1 s during which time the participant implemented the corresponding mental imagery once. After 1 s, the action stimulus disappeared and a random duration off-time of 1.5–2.5 s followed, concluding the trial. The trial procedure was repeated 300 times per interaction segment, resulting in a total segment duration of 15 min
- Hand movement is especially potent, due to easily distinguishable activity in the contra-lateral cortical regions responsible for the movement of the limbs, located directly under C3, C4, T3, T4 and Cz sites of the standard 10/20 international system.
  - Thus, EEG-based discrimination of left- and right-hand MI based on contra-laterally localized activity observed via C3 and C4 electrodes has become one of the most easily deployable EEG BCI communication paradigms.
  - Thus, our “Paradigm #1 – CLA (Classical)” includes a similar EEG BCI interaction model based on three imageries of left and right-hand movements and one passive mental imagery in which participants remained neutral and engaged in no motor imagery.
- Many other paradigms also available.



* * *
* * *
© [Lennert Bontinck](https://www.lennertbontinck.com/) VUB 2021-2022