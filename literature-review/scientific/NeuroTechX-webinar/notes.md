# NeuroTechX Webinar 2018

According to [NeuroTechX's website](https://neurotechx.com/), NeuroTechX (NTX) is a non-profit organization whose mission is to facilitate the advancement of neurotechnology by providing key resources and learning opportunities, and by being leaders in local and worldwide technological initiatives. On their [YouTube channel](https://www.youtube.com/c/NeuroTechX) many BCI related videos are available. This document gives some notes that were taken whilst watching their webinars from 2018 to 2019, webinar 1 to 9. This playlist is available [here](https://www.youtube.com/watch?v=AFKNbNBCtXs&list=PL7yYIG1eq9bTbK-W66TCl7t8wTXwelSNz). The notebooks from the video are available [here](https://github.com/NeuroTechX/eeg-notebooks).



## Table of contents

- [Contact information](#contact-information)
- 

<hr>


## Contact information

| Name             | Role                 | VUB mail                                                  | Personal mail                                               |
| ---------------- | -------------------- | --------------------------------------------------------- | ----------------------------------------------------------- |
| Lennert Bontinck | Master Thesis writer | [lennert.bontinck@vub.be](mailto:lennert.bontinck@vub.be) | [info@lennertbontinck.com](mailto:info@lennertbontinck.com) |

<hr>


## NeuroTechX Webinar #1: EEG Notebooks

This webinar is available [here](https://youtu.be/AFKNbNBCtXs). The host of the webinar was Sydney Swaine-Simon. The speaker discussing the notebook was Dano Morrison.

- Dano Morrison spoke about the Jupyter Notebooks made by NTX. These notebooks aim to make working with EEG for a first time more accessible.
- They used Muse LSL to connect devices which makes use of pygatt, pylsl and BlueMuse (thus based on **Lab Streaming Layer**)
- Stimulus presentation happens through **PsychoPy**
- Data analysis happens through **MNE**
- Data visualization happens through **MatPlotLib**
- He went through the N170 notebook
   - The N170 is a large negative event-related potential (ERP) component that occurs after the detection of faces, but not objects, scrambled faces, or other body parts such as hands.
- They used a **MUSE headband** (MUSE 2016)
   - This is one of the early commercial BCIs with somewhat widespread adoption. Used for focus etc.
- 2 minute trials are often a good idea because it will lead to less errors and noise since user will have ability to focus for the whole length
- They did an experiment in the notebook where you watch flashing images, some of houses others of faces. The faces should trigger the N170. This can be used for "live" classification accuracy testing as well.
   - He said this is *not so fun* but it is needed for around 3 - 6 times for 2 minutes each. This is an issue with data collection for BCI applications.
- Again, peaks at some random frequencies (Hz's) - e.g. **60hz peak for electrical wires**.
- Often a "low level pass" -> **filter out lower frequencies, e.g. 0 - 30**. All of this easy with MNE.
- **Epoching of data** -> split continues data in smaller data frames. Here for reaction to faces or other objects +- 100ms before and 800ms after stimulus.
   - So your data should be labelled what is seen/done when. Otherwise it is just random data.
- Was shown how deflection (negative impulse) is visible in face recognition. Thus experiment was successful. 
- Uses **SciKit pipelines** and classifiers to test different performance aspects.



<hr>

## NeuroTechX Webinar #2: BCI/EEG in VR/AR

This webinar is available [here](https://youtu.be/Rggx_YVc6CM). The host of the webinar was Yannick Roy.




* * *
* * *
© [Lennert Bontinck](https://www.lennertbontinck.com/) VUB 2021-2022