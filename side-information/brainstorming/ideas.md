# Draft for ideas

This document is a draft where plausible ideas can be quickly noted down so they can be explored further later on.

## Table of contents

- [Author](#author)
- [Ideas](#ideas)


<hr>


## Author

| Name             | Role                 | VUB mail                                                  | Personal mail                                               |
| ---------------- | -------------------- | --------------------------------------------------------- | ----------------------------------------------------------- |
| Lennert Bontinck | Master Thesis writer | [lennert.bontinck@vub.be](mailto:lennert.bontinck@vub.be) | [info@lennertbontinck.com](mailto:info@lennertbontinck.com) |

<hr>


## Ideas

- *Simulate* OpenBCI data from medical BCI data
  - Reduce hertz and accuracy
  - Introduce more noise
  - Select right amount of sensors
- Check which locations of sensors are most important for the application to know best placement in OpenBCI
  - Do this e.g. by LOO so that unimportant sensors/measurements can be determined
- Playing around with pre-processing before OpenBCI conversion
- Using visual cortex for start stop command
  - E.g. closing eyes for certain period of time brakes and then halts system
  - E.g. looking at a certain screen (flashing) starts the system
- Using camera's or lidar or sonar or... to detect if requested move (e.g. left turn) would result in a crash and thus make it ignored
- When many wrong signals are received (e.g. crash actions), ask for retraining
- Error signal recognition to determine if performed action is wrong 

* * *
* * *
© [Lennert Bontinck](https://www.lennertbontinck.com/) VUB 2021-2022