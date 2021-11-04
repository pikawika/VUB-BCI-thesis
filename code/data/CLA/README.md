# CLA Dataset

This folder should contain the CLA variant of the dataset provided by [Kaya et al](https://doi.org/10.1038/sdata.2018.211).

<hr>

## Table of contents

- [Contact information](#contact-information)
- [Data available](#data-available)
- [Files to download](#files-to-download)

<hr>

## Contact information

| Name             | Role                 | VUB mail                                                  | Personal mail                                               |
| ---------------- | -------------------- | --------------------------------------------------------- | ----------------------------------------------------------- |
| Lennert Bontinck | Master Thesis writer | [lennert.bontinck@vub.be](mailto:lennert.bontinck@vub.be) | [info@lennertbontinck.com](mailto:info@lennertbontinck.com) |

<hr>

## Files to download

In total 16 CLA files should be placed here, of which 3 are of type `inter`. These files can be downloaded from [here](https://doi.org/10.6084/m9.figshare.c.3917698.v1). All files that should be downloaded are:

- CLA-SubjectJ-170504-3St-LRHand-Inter.mat
- CLA-SubjectJ-170508-3St-LRHand-Inter.mat
- CLA-SubjectJ-170510-3St-LRHand-Inter.mat
- CLASubjectA1601083StLRHand.mat
- CLASubjectB1510193StLRHand.mat
- CLASubjectB1512153StLRHand.mat
- CLASubjectC1511263StLRHand.mat
- CLASubjectC1512163StLRHand.mat
- CLASubjectC1512233StLRHand.mat
- CLASubjectD1511253StLRHand.mat
- CLASubjectE1512253StLRHand.mat
- CLASubjectE1601193StLRHand.mat
- CLASubjectE1601223StLRHand.mat
- CLASubjectF1509163StLRHand.mat
- CLASubjectF1509173StLRHand.mat
- CLASubjectF1509283StLRHand.mat

<hr>

## Data available

The following data is available:

- id: A unique alphanumeric identifier of the record
- tag: Unknown field
   - Was not specified in the article
- binsuV: Probably bins per microvolt
   - Was not specified in the article
- nS: Number of EEG data samples
- sampFreq: Sampling frequency of the EEG data
- marker: The eGUI interaction record of the recording session
   - 0: “blank” or nothing is displayed in eGUI
      - Can be seen as a break between stimuli, thus random EEG data that should probably be ignored
   - 1: Left hand action
       - EEG data for MI of the left hand
   - 2: Right hand action
       - EEG data for MI of the right hand
   - 3: Passive/neutral
       - EEG data for MI of neither left nor right hand
- chnames: Probably channel names of the EEG data sensors/channels in 10/20 configuration
   - Was not specified in article
- data: The raw EEG data of the recording session

## Information about the dataset

The below information is provided by the `Dataset description file` available on [the download page of the dataset](https://doi.org/10.6084/m9.figshare.c.3917698.v1).

**Subject annotation**
SUBJECTX wit X ranging A-Z

**Dataset variants**
5F= FIVE FINGERS
CLA=CLASSIC
FREEFORM=FREE STYLE 5F
HaLT=HAND LEG TONGUE
NoMT=NO MOTOR

**Actions**
L= Left
R= Right
F= Finger
H= High
SGL= Single
Freq= Frequency
Tong= Tongue
St=State
Inter=Interactive Interface

**Date**
2016 APRIL 08= 160508(YYMMDD)

**Subject's information**
SUBJECTA - Male, 20-25 y.o.
SUBJECTB - Male, 20-25 y.o.
SUBJECTC - Male, 25-30 y.o.
SUBJECTD - Male, 25-30 y.o.
SUBJECTE - Female, 20-25 y.o.
SUBJECTF - Male, 30-35 y.o.
SUBJECTG - Male, 30-35 y.o.
SUBJECTH - Male, 20-25 y.o.
SUBJECTI - Female, 20-25 y.o.
SUBJECTJ - Female, 20-25 y.o.
SUBJECTK - Male, 20-25 y.o.
SUBJECTL - Female, 20-25 y.o.
SUBJECTM - Female, 20-25 y.o.

**Electrode order (1-22)**
Fp1 Fp2 F3 F4 C3 C4 P3 P4 O1 O2 A1 A2 F7 F8 T3 T4 T5 T6 Fz Cz Pz X3

**Marker codes**
CLA, HaLT, FreeForm interaction paradigm
1-left hand MI, 2-right hand MI, 3-passive state, 4-left leg MI, 5-tongue MI, 6-right  leg MI

**5F interaction paradigm**
1-thumb MI, 2-index finger MI, 3-middle finger MI, 4-ring finger MI, 5-pinkie finger MI

**all paradigms**
99-initial relaxation period
91-inter-session rest break period
92-experiment end

**Other notes**
-HFREQ are the data recorded with 1000 Hz sampling setting on the Nihon Kohden EEG-1200 device. That data files differ from the other files in higher sampling frequency, namely 1000 Hz vs. 200 Hz for other data.
-Inter are the data recorded for the indicated interaction paradigm by using the custom interactive brain-computer interface software. That data differs from the other files by a different signal resolution and signal's dynamic range, namely the signal resolution of 0.133uV vs. 0.01uV in the other data, and the dynamic range of +/-121.6uV vs. better than +/-2mV in the rest of the data.
-CLA-SubjectF-150916-3St-LRHand is one of our earliest BCI experiments and for that reason contains only two BCI signals - left and right hand movements, without passive imagery.

* * *
* * *
© [Lennert Bontinck](https://www.lennertbontinck.com/) VUB 2021-2022