# Initialisation of the Anaconda environment

When the Anaconda environment was setup using [the provided install instructions](../installation/README.md), the environment can easily be initialised. These instruction discuss how that can be done.

## Table of contents

- [Author](#author)
- [Windows](#windows)
   - [Windows initialisation script](#windows-initialisation-script)
- [MacOS](#macos)
   - [MacOS initialisation script](#macos-initialisation-script)

<hr>


## Author

| Name             | Role                 | VUB mail                                                  | Personal mail                                               |
| ---------------- | -------------------- | --------------------------------------------------------- | ----------------------------------------------------------- |
| Lennert Bontinck | Master Thesis writer | [lennert.bontinck@vub.be](mailto:lennert.bontinck@vub.be) | [info@lennertbontinck.com](mailto:info@lennertbontinck.com) |

<hr>


## Windows

### Windows Initialisation script

The below script can be used to start the anaconda environment in the GitHub project folder and launch a Jupyter Notebook server.

```shell
# Launches the correct environment from the install instructions
CALL conda activate bci-master-thesis

# Launches Jupyter Notebook server on correct folder.
# Replace <path-of-github> with your source of the GitHub repository.
#   e.g. D:\Libraries\Documenten\GitHub\bci-master-thesis
CALL jupyter notebook --notebook-dir="<path-of-github>"
```

<hr>


## MacOS

### MacOS Initialisation script

The below script can be used to start the anaconda environment in the GitHub project folder and launch a Jupyter Notebook server.

```shell
# Replace <path-of-conda> with your source of the conda.sh file.
#   e.g. /Users/lennertbontinck/opt/anaconda3/etc/profile.d/conda.sh
source <path-of-conda>
# Launches the correct environment from the install instructions
conda activate bci-master-thesis
# Replace <path-of-github> with your source of the GitHub repository.
#   e.g. /Users/lennertbontinck/Documents/GitHub/bci-master-thesis
cd <path-of-github>
# Launches Jupyter Notebook server
jupyter notebook
```



* * *
* * *
© [Lennert Bontinck](https://www.lennertbontinck.com/) VUB 2021-2022