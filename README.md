# Image Converter

**Made with <3 by [Amazing Cow](http://www.amazingcow.com).**



<!-- ####################################################################### -->
<!-- ####################################################################### -->

## Description:

```imgconv``` - Convert images formats with ease.

```imgcov``` is a small tool to convert between images formats.    
The images (the input and output) must be in any image format supported by 
[pygame](http://www.pygame.org). 


<br>

As usual, you are **very welcomed** to **share** and **hack** it.



<!-- ####################################################################### -->
<!-- ####################################################################### -->

## Usage:

``` 
  imgconv -h | -v | -l
  imgconv [-V] [-F] [-o <path>] [-f <format>] [-n] start-path

Options:
 *-h --help          : Show this screen
 *-v --version       : Show app version and copyright.
 *-L --list-formats  : Show the supported output formats.

  -V --verbose          : Verbose mode, helps to see what it's doing.
  -F --force            : Force the conversion even if it's not need.
  -o --output <path>    : Directory that converted images will be placed.
  -f --format <format>  : Format of converted images (See --list-formats).

  -n --no-color : Print the output without colors.

Notes:
  If <start-path> is blank the current dir is assumed.
  If --output <path> is not specified the ./imgconv_output will be assumed.
  If --format <format> is not specified the [png] format will be assumed.

  Options marked with * are exclusive, i.e. the imgconv will run that
  and exit after the operation.
```


<!-- ####################################################################### -->
<!-- ####################################################################### -->

## Install:

Use the Makefile.

``` bash
    make install
```

Or to uninstall

``` bash
    make uninstall
```



<!-- ####################################################################### -->
<!-- ####################################################################### -->

## Dependencies:

This project uses / depends on:

* Amazing Cow's 
[cowtermcolor](http://www.github.com/AmazingCow-Libs/cowtermcolor_py)
package to coloring the terminal.

* [pygame](http://www.pygame.org) as a backend to image manipulations.



<!-- ####################################################################### -->
<!-- ####################################################################### -->

## Environment and Files: 

```imgconv``` do not create / need any other files or environment vars.



<!-- ####################################################################### -->
<!-- ####################################################################### -->

## License:

This software is released under GPLv3.



<!-- ####################################################################### -->
<!-- ####################################################################### -->

## TODO:

Check the TODO file for general things.

This projects uses the COWTODO tags.   
So install [cowtodo](http://www.github.com/AmazingCow-Tools/COWTODO) and run:

``` bash
$ cd path/for/the/project
$ cowtodo 
```

That's gonna give you all things to do :D.



<!-- ####################################################################### -->
<!-- ####################################################################### -->

## BUGS:

We strive to make all our code the most bug-free as possible - But we know 
that few of them can pass without we notice ;).

Please if you find any bug report to [bugs_opensource@amazingcow.com]() 
with the name of this project and/or create an issue here in Github.



<!-- ####################################################################### -->
<!-- ####################################################################### -->

## Source Files:

* AUTHORS.txt
* CHANGELOG.txt
* COPYING.txt
* imgconv.py*
* Makefile
* README.md
* TODO.txt



<!-- ####################################################################### -->
<!-- ####################################################################### -->

## Others:
Check our repos and take a look at our [open source site](http://opensource.amazingcow.com).
