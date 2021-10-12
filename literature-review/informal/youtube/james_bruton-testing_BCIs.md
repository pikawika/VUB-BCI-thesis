# Testing Brain-Computer Interfaces by James Bruton

This file contains some documentation on the Testing Brain-Computer Interfaces [YouTube video](https://youtu.be/TMeJyrPmwwM) by James Bruton. James Bruton is not an expert in the field, in fact, he's pretty new to the field. However, the video is a playfull first sight on the topic and some of the comments are helpfull starting points.

## Table of contents

- [Author](#author)
- [What is interesting](#what-is-interesting)
  * [From the video](#from-the-video)
  * [From the comments](#from-the-comments)

<hr>


## Author

| Name             | Role                 | VUB mail                                                  | Personal mail                                               |
| ---------------- | -------------------- | --------------------------------------------------------- | ----------------------------------------------------------- |
| Lennert Bontinck | Master Thesis writer | [lennert.bontinck@vub.be](mailto:lennert.bontinck@vub.be) | [info@lennertbontinck.com](mailto:info@lennertbontinck.com) |

<hr>


## What is interesting

### From the video

- OpenBCI offers both an assembled headset and a non assembled one where you need to 3D print the headset enclosure yourself. The latter is cheaper and makes BCIs affordable.
- The kit has 8 (Cyton board) or 16 channels (Cyton with Daisy extension) and a Bluetooth connection.
- The kit also comes with *blanks* that are used to fill the remaining holes and help with making the headset more comfortable.
- The sensors have differing ends, where the longer tips are supposed to be more comfortable for long term wearing. Perhaps they are less accurate?
- OpenBCI is open-source.
- 2 clips are placed on both ears for ground reference. Their position is important to be more/most accurate. James recommends the top of the ear rather than the bottom and uses the *railed status* as a guideline.
- The headset is prone to noise, on 6:15 he discussed that the 50hz channel has artefacts due to the electrical wiring in the wall working on that frequency. He also noticed a spike in 20hz from his laptop if he sits too close.
-  He also discusses that muscle motion such as closing eyes is detected which are not EEG data and thus in a way also *artefacts*, however as these are easily noticeable and are in a way useful they might be handy input.
- Band power in OpenBCI GUI bins the frequencies in the known named frequencies such as Delta, Theta, ...
  - Higher frequencies such as gamma waves are more thought related whilst lower ones are more motion-related.
  - You can play with this yourself to see what happens when you do certain things. 
- In the OpenBCI GUI you can see the *railed* status, which tells you about the connection. It uses the ground reference for this.
- Hydrated skin also seems to have an influence - conduction after eating and drinking water was better. This shows the OpenBCI is rather sensitive to these types of things.
- Know the different locations of the brain, such as the motor cortex and visual cortex, which might be more/less interesting for the application.
- Motor cortex seems to be a tough one to detect, especially with the default headset. At 14:10 he discussed a custom headset designed for *motor cortex only targeting*. 
- At 16:50, it becomes clear that even slightly moving the BCI has a drastic impact on the findings and data. Perhaps some trick to *correctly position the headset* exists.
- It is more difficult to read thoughts, on the frontal side of the brain, than to read the motor cortex which is from one ear to the other. The backside contains more of the visual cortex.



### From the comments

Some of the comments are rather helpful in things to look out for, some extracts are given here.

- Some of the comments point out that James is no expert in the field as some of the things he said *are just plain wrong*.
- You are confronting at least two problems here.
  - One is using just a few electrodes on the scalp to attempt to localize signals from a specific part of the brain. This is known as the "inverse" problem, and it's non-trivial, to say the least. 
  - The second problem is trying to pick up signals that convincingly correlate to some pattern of thought. Those are quite small signals relative to the coarse waves seen at an electrode that represents the sum of the activity of thousands or millions of neurons near that electrode.  To detect such a signal, experimenters use a paradigm like: present the experimental subject with a succession of trials, repeating the same stimulus over and over again (intermingled with control different-stimulus trials), and then average the signals from like trials together, aligned to the time of the stimulus onset.  Then subtract the average control signal from that of the stimulus trials to produce a result signal.  Hoping to discern a thought with a single trial, no controlled trial, and no sync to stimulus is pretty optimistic.
- It is discussed how **noise is a big problem with these types of headsets**
  - You always have to worry about what you are actually measuring. EEG picks up magnetic fields on the skin. Anything that can cause those fields can produce a signal, like your 50Hz line noise. Around [7:20](https://www.youtube.com/watch?v=TMeJyrPmwwM&t=440s), you may be producing a muscle signal ever so slightly on your scalp.  Try clenching your jaw next time you wear the headset. You'll clearly see the muscle signal. 
- The problem with EEG sensors is that blood pressure will have an effect, you've can see that when you tense your muscles and it lights up your whole brain, it's not brain activity though, it's the blood that is going to your head rather than to your constricted extremities. Biosensing of the core blood pressure typically positioned on the lower neck or chest can be used as a point of reference to interpret the sensor data filtering out blood pressure. While Cerebral blood flow is decoupled from body blood pressure, you still have the skin and muscle over the skull with bodily blood pressures interfering with the probes.

* * *
* * *
© [Lennert Bontinck](https://www.lennertbontinck.com/) VUB 2021-2022