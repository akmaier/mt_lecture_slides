[![pipeline status](https://git5.cs.fau.de/teaching/MT1-lecture/badges/master/pipeline.svg)](https://git5.cs.fau.de/teaching/MT1-lecture/pipelines)

# Medizintechnik 2 – Lecture Slides

This repo has submodules. So clone with 

    git clone --recurse-submodules -j8 git@git5.cs.fau.de:teaching/MT1-lecture.git

There are symlinks to the LME beamer theme in each folder.
This works only on Linux and MacOS.
Windows users could copy the theme in the respective folders or change the theme folder in the preamble.

## TODOs

 - US
 - extend OCT-A?

- Link to this demo: http://www.jezzamon.com/fourier/index.html

Teach students about exception breakpoints in exercise slides:

 - https://stackoverflow.com/questions/3066199/break-when-exception-is-thrown
 - IntelliJ: Run | View Breakpoints | Exception Breakpoints

For excercise:

Enable this flag automatically in exercises. Java is not helpful by default.
```
Helpful NullPointerExceptions describing precisely which variable was null
JDK 14 (enabled with -XX:+ShowCodeDetailsInExceptionMessages)

a.b.c.i = 99;
---
Exception in thread "main" java.lang.NullPointerException:
      Cannot read field "c" because "a.b" is null
```

## PDFs

You can download the latest PDFs from the [CI](https://git5.cs.fau.de/teaching/MT1-lecture/pipelines).
There is a download button for most commits.
Rebuild if necessary.

## Build everything 

```bash
make s00; make s01; make s02; make s03; make s04; make s05; make s05_2; make s06; make s07; make s07_2; make s08; make s09; make s10; make s11
```
(requires `latexmk`)
