# VUB LaTeX huisstijl

This repository contains all needed files to typeset your LaTeX
documents in the huisstijl-style of the Vrije Universiteit Brussel:

![Example typeset title page](http://i.imgur.com/hDvfwVj.png)

## Installation

### Overleaf

Overleaf is full of templates that are based on this code.  Most of them are
not up to date.  If you find an out-of-date template, please contact me or
Overleaf to have them update or remove it.

Instead of hosting the templates on Overleaf (which is tiresome to update), you
can use these links to start from a template.

- [![](https://www.rubdos.be/open-in-overleaf.png) VUB-styled article](https://www.overleaf.com/docs?snip_uri=https://gitlab.com/rubdos/texlive-vub/-/jobs/artifacts/master/raw/templates/template-vub-article.zip?job=template-zips)
- [![](https://www.rubdos.be/open-in-overleaf.png) VUB-styled thesis](https://www.overleaf.com/docs?snip_uri=https://gitlab.com/rubdos/texlive-vub/-/jobs/artifacts/master/raw/templates/template-vub-thesis.zip?job=template-zips)
- [![](https://www.rubdos.be/open-in-overleaf.png) Bruface-styled thesis](https://www.overleaf.com/docs?snip_uri=https://gitlab.com/rubdos/texlive-vub/-/jobs/artifacts/master/raw/templates/template-bruface-thesis.zip?job=template-zips)
    *This might be out-of-date*, [patches are welcome](https://gitlab.com/rubdos/texlive-vub/-/merge_requests/new).
- [![](https://www.rubdos.be/open-in-overleaf.png) VUB-styled presentation](https://www.overleaf.com/docs?snip_uri=https://gitlab.com/rubdos/texlive-vub/-/jobs/artifacts/master/raw/templates/template-vub-presentation.zip?job=template-zips)

### Local usage (all operating systems)

Windows and macOS (and other) users [can download a zip file](https://gitlab.com/rubdos/texlive-vub/repository/archive.zip?ref=v2.4.2)
containing the latest version. As of writing, that's v2.4.2.

You can also [download the development version](https://gitlab.com/rubdos/texlive-vub/repository/archive.zip?ref=master).

This `.zip`-file contains (among others) `.sty` files and `vub_logo_cmyk.pdf`.
Put these files in your project directory.

Alternatively, you can download a template from any of these:

- [VUB-styled article](https://gitlab.com/rubdos/texlive-vub/-/jobs/artifacts/master/raw/templates/template-vub-article.zip?job=template-zips)
- [VUB-styled thesis](https://gitlab.com/rubdos/texlive-vub/-/jobs/artifacts/master/raw/templates/template-vub-thesis.zip?job=template-zips)
- [Bruface-styled thesis](https://gitlab.com/rubdos/texlive-vub/-/jobs/artifacts/master/raw/templates/template-bruface-thesis.zip?job=template-zips)
    *This might be out-of-date*, [patches are welcome](https://gitlab.com/rubdos/texlive-vub/-/merge_requests/new).
- [VUB-styled presentation](https://gitlab.com/rubdos/texlive-vub/-/jobs/artifacts/master/raw/templates/template-vub-presentation.zip?job=template-zips)

### Arch Linux

[For Arch Linux users, I made an AUR package](https://aur.archlinux.org/packages/texlive-vub/)
called `texlive-vub`. Just `pacaur -S texlive-vub` and roll on.
If you're planning on using the beamer theme, install the optional dependencies:
`ttf-roboto` for XeLaTeX/LuaLaTeX, or `texlive-fontsextra` for pdflatex.

### Debian dependencies

Apart from the usual texlive dependencies, you will need `texlive-latex-extra`
(which contains `colorspace`) and `tex-gyre` for pdfLaTeX, or `fonts-texgyre` for XeLaTeX.
Those font packages do need feedback though. Please let me know if they work!

You will also need `fonts-roboto` (jessie-backports) if you want to use `beamer` with XeTeX.
*Do not install `fonts-roboto-fontface` on Buster*, since it contains `.woff` style fonts,
which is mentioned in `fontconfig` in Buster, but [XeTeX cannot handle these](https://sourceforge.net/p/xetex/bugs/139/).
See also [this tracking issue](https://gitlab.com/rubdos/texlive-vub/issues/30).

### Windows XeLaTeX/LuaLaTeX notice

You will have to manually install the Roboto fonts in order for the `beamer` theme to work.
On pdfLaTeX, this should automatically work, since MikTeX includes roboto fonts for pdfLaTeX.

### Important notice to website maintainers and Overleaf templaters.

I will regularly update this repository,
and so the files and instructions *will* change.
If you would like to post this on your website,
please provide *a link to this GitLab webpage*. Do **not** rehost the `.zip` file.

## Usage

### article/report

Note: `vub` and `bruface` are now interchangeable for articles/reports.
`bruface` will create a [Bruface](http://bruface.eu/) title page, with the ULB and Bruface logo's included.
This is a very early and untested version; please report back using the [GitLab issue tracker](https://gitlab.com/rubdos/texlive-vub/issues).

```
\documentclass{article}
\usepackage{vub} % this will automatically set to A4 paper. We're not in the US.
% if, for some obscure reason, you need another format, please file an issue (see further).
\title{Your Title Here}
\subtitle{An optional Subtitle Here}
\faculty{Sciences and Bio-Engineering Sciences} % Note: without the word "Faculty"!
\author{John Doe}

...

\begin{document}
\maketitle
\end{document}
```

Will give your article a title page.

If you want spotcolors in your pdf (only pdfLaTeX for now), add the spotcolors option
when including the package:

```
...
\usepackage[spotcolors]{vub}
...
```

If you are doing a thesis, you probably want to include your promotors' names, and some "pre-title"
(e.g. "Proef ingediend met het oog op het behalen van de graad van bachelor in de
 Farmaceutische wetenschappen").
`texlive-vub` supports this; put something like this in your preamble:

```
\promotors{My Promotor, Another Promotor}
\pretitle{Proef ingediend met het oog op het behalen van de graad van ... }
```

### Beamer/powerdot slides

```
\documentclass{beamer}
\usetheme{vub} % This will automatically load all fonts (Roboto and TeX Gyre Adventor
               % for titles), and the VUB colors. Also includes the triangle.
\title{Your title}
%\subtitle{Your subtitle} % Can be omitted
\author{John Doe}

...

\begin{document}
\frame{\maketitle} % Automatic titlepage with VUB logo.
\end{document}
```

Several options can be specified when loading the vub theme.

```
\usetheme[coloredtitles]{vub}
```

will use colored bars as background for the title on a slide.

```
\usetheme[coloredblocks]{vub}
```

will use the vub colors as background for block environments (such as theorems).

```
\usetheme[showsection]{vub}
```

will show the current section name on each slide.

Additionally, you can set the `dept` option to use the combined logo of your department.
Currently, ETRO, SOFT, AI and Brubotics logo's are included:

```
\usetheme[dept=etro]{vub} % or
\usetheme[dept=soft]{vub} % or
\usetheme[dept=ai]{vub} % or
\usetheme[dept=brubotics]{vub}
```


Finally, you can include a small copyright notice or acknowledgement on the title page using 

```
\usetheme[copyright={Slides are mainly due to Jane Doe}]{vub}
```


### bruface notes

If you are in Bruface programme, this package can set your MSc thesis' title page.
If you want to do this, please provide at least your `\programme`, `\supervisor` and set `\date` to the academic year:

```
\supervisor{Prof. John Doe}
% \cosupervisor{John Doe PhD} % optional
\programme{Engineering science bla}
\date{2017-2018}
```

## Supported compilers

Currently supported:

- `pdfLaTeX` (the most common LaTeX compiler)
- `XeLaTeX`

Supported, but untested:

- `LuaLaTeX`

This package currently contains code for the **title page** of articles and reports,
and for **beamer** (non corporate) presentations.

**beamer** only is for "internal" style currently.
Corporate style is on the [TODO list](https://gitlab.com/rubdos/texlive-vub/issues/6),
and will be an option in the `\usetheme{vub}` command in the future.
Please vote on that issue if you need this.

I might have `powerdot` support [sooner or later](https://gitlab.com/rubdos/texlive-vub/issues/7),
in this very same package; I'll then try to support both corporate and internal style.
Please vote on that issue if you need it.

I tried to keep as close as possible to [the original huisstijlgids](http://huisstijl.vub.ac.be/)
from the VUB.
I got the positions of images and text from the dotx Microsoft Word document (holy crap),
and sourced the *vector* logo from the huisstijl downloads (converted the eps to pdf,
rehosted in this repo for convenience).
The small triangle is a TikZ oneliner.

## Licensing

LaTeX packages are usually covered by the LPPL. This is no exception:

     Copyright 2016-2020 Ruben De Smet

    This work may be distributed and/or modified under the
    conditions of the LaTeX Project Public License, either version 1.3
    of this license or (at your option) any later version.
    The latest version of this license is in
      http://www.latex-project.org/lppl.txt
    and version 1.3 or later is part of all distributions of LaTeX
    version 2005/12/01 or later.

    This work has the LPPL maintenance status `maintained'.

    The Current Maintainer of this work is Ruben De Smet.

    This work consists of the files vub.sty, test.tex and Makefile.


Of course, I am in no position to license the VUB logo; you have to provide a
license for that yourself. The logo is provided solely as a convenience in this repo.

Everything else in this repository falls under the LPPL as previously stated.

## Contributing

Please be smart; if you change something to the `.sty` file, chances are _very_ high
that someone else is interested in the exact same change.
Please file a merge request, or send me an email.
My VUB netID is `rubedesm`; if you don't know what that is, you'll find my e-mail adress
[on my website](https://www.rubdos.be/consulting/), at the bottom of my consulting page.
Heck, my phone number's even there, just give me a call already.

If you know that a bunch of people use a certain GNU/Linux distribution and you think
it'll be useful to have a package for it, make an issue, or otherwise contact me. I already
had a request for Debian and Fedora, so they'll probably follow.
