#!/usr/bin/python
#coding=utf8
##----------------------------------------------------------------------------##
##               █      █                                                     ##
##               ████████                                                     ##
##             ██        ██                                                   ##
##            ███  █  █  ███        imgconv.py                                ##
##            █ █        █ █        ImageConverter                            ##
##             ████████████                                                   ##
##           █              █       Copyright (c) 2016                        ##
##          █     █    █     █      AmazingCow - www.AmazingCow.com           ##
##          █     █    █     █                                                ##
##           █              █       N2OMatt - n2omatt@amazingcow.com          ##
##             ████████████         www.amazingcow.com/n2omatt                ##
##                                                                            ##
##                  This software is licensed as GPLv3                        ##
##                 CHECK THE COPYING FILE TO MORE DETAILS                     ##
##                                                                            ##
##    Permission is granted to anyone to use this software for any purpose,   ##
##   including commercial applications, and to alter it and redistribute it   ##
##               freely, subject to the following restrictions:               ##
##                                                                            ##
##     0. You **CANNOT** change the type of the license.                      ##
##     1. The origin of this software must not be misrepresented;             ##
##        you must not claim that you wrote the original software.            ##
##     2. If you use this software in a product, an acknowledgment in the     ##
##        product IS HIGHLY APPRECIATED, both in source and binary forms.     ##
##        (See opensource.AmazingCow.com/acknowledgment.html for details).    ##
##        If you will not acknowledge, just send us a email. We'll be         ##
##        *VERY* happy to see our work being used by other people. :)         ##
##        The email is: acknowledgment_opensource@AmazingCow.com              ##
##     3. Altered source versions must be plainly marked as such,             ##
##        and must not be misrepresented as being the original software.      ##
##     4. This notice may not be removed or altered from any source           ##
##        distribution.                                                       ##
##     5. Most important, you must have fun. ;)                               ##
##                                                                            ##
##      Visit opensource.amazingcow.com for more open-source projects.        ##
##                                                                            ##
##                                  Enjoy :)                                  ##
##----------------------------------------------------------------------------##

## Imports ##
import getopt;
import os.path;
import os;
import sys;
import pdb;


################################################################################
## Don't let the standard import error to users - Instead show a              ##
## 'nice' error screen describing the error and how to fix it.                ##
################################################################################
def __import_error_message_print(pkg_name, pkg_url):
    print "Sorry, "
    print "imgconv depends on {} package.".format(pkg_name);
    print "Visit {} to get it.".format(pkg_url);
    print "Or checkout the README.md to learn other ways to install {}.".format(pkg_name);
    exit(1);


## cowtermcolor ##
try:
    from cowtermcolor import *;
except ImportError, e:
    __import_error_message_print(
        "cowtermcolor",
        "http//opensource.amazingcow.com/cowtermcolor.html");

## pygame ##
try:
    import pygame;
except ImportError, e:
    __import_error_message_print(
        "pygame",
        "http//www.pygame.org");



################################################################################
## Globals                                                                    ##
################################################################################
class Globals:
    verbose     = False;

    start_path  = ".";
    output_path = "./imgconv_output";

    output_format  = "png";

    force_conversion = False;


################################################################################
## Constants                                                                  ##
################################################################################
class Constants:
    ## Flags ##
    #Exclusives
    FLAG_HELP        = "h", "help";
    FLAG_VERSION     = "v", "version";
    FLAG_DISPLAY_EXT = "L", "list-formats";
    #Optionals
    FLAG_VERBOSE        = "V", "verbose";
    FLAG_FORCE          = "F", "force";
    FLAG_OUTPUT_PATH    = "o", "output";
    FLAG_OUTPUT_FORMAT  = "f", "format";
    FLAG_NO_COLORS      = "n", "no-colors"

    ALL_FLAGS_SHORT = "".join([
        FLAG_HELP          [0],
        FLAG_VERSION       [0],
        FLAG_DISPLAY_EXT   [0],
        FLAG_VERBOSE       [0],
        FLAG_FORCE         [0],
        FLAG_OUTPUT_PATH   [0] + ":",
        FLAG_OUTPUT_FORMAT [0] + ":",
        FLAG_NO_COLORS     [0],
    ]);
    ALL_FLAGS_LONG = [
        FLAG_HELP          [1],
        FLAG_VERSION       [1],
        FLAG_DISPLAY_EXT   [1],
        FLAG_VERBOSE       [1],
        FLAG_FORCE         [1],
        FLAG_OUTPUT_PATH   [1] + "=",
        FLAG_OUTPUT_FORMAT [1] + "=",
        FLAG_NO_COLORS     [1],
    ];

    ## Formats ##
    SUPPORTED_FORMATS      = ["bmp", "tga", "png", "jpg", "jpeg"];
    SUPPORTED_FORMATS_BMP  = SUPPORTED_FORMATS[0];
    SUPPORTED_FORMATS_TGA  = SUPPORTED_FORMATS[1];
    SUPPORTED_FORMATS_PNG  = SUPPORTED_FORMATS[2];
    SUPPORTED_FORMATS_JPG  = SUPPORTED_FORMATS[3];
    SUPPORTED_FORMATS_JPEG = SUPPORTED_FORMATS[4];

    # App ##
    APP_NAME      = "imgconv";
    APP_VERSION   = "0.2.1";
    APP_AUTHOR    = "N2OMatt <n2omatt@amazingcow.com>"
    APP_COPYRIGHT = "\n".join(("Copyright (c) 2016 - Amazing Cow",
                               "This is a free software (GPLv3) - Share/Hack it",
                               "Check opensource.amazingcow.com for more :)"));



################################################################################
## Colors Stuff                                                               ##
################################################################################
ColorError      = Color(RED);
ColorWarning    = Color(YELLOW);
ColorOK         = Color(GREEN);
ColorPath       = Color(MAGENTA);
ColorInfo       = Color(BLUE);
ColorProcessing = Color(YELLOW);



################################################################################
## Print Functions                                                            ##
################################################################################
def print_verbose(msg):
    if(Globals.verbose):
        print msg;


def print_fatal(msg):
    print ColorError("[FATAL]"), msg;
    exit(1);

def print_error(msg):
    print ColorError("[ERROR]"), msg;

def print_help(exit_code = -1):
    msg = """Usage:
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
"""
    print msg;

    if(exit_code != -1):
        exit(exit_code);


def print_version(exit_code = -1):
    print "{} - {} - {}".format(Constants.APP_NAME,
                                Constants.APP_VERSION,
                                Constants.APP_AUTHOR);
    print Constants.APP_COPYRIGHT;
    print;

    if(exit_code != -1):
        exit(exit_code);


def print_formats(exit_code = -1):
    print "{} - {} - {}".format(Constants.APP_NAME,
                                Constants.APP_VERSION,
                                "AmazingCow");

    print "Output formats supported: ";
    print "   " + " - ".join(Constants.SUPPORTED_FORMATS);

    if(exit_code != -1):
        exit(exit_code);


def print_run_info():
    print_verbose("Run info");
    print_verbose("  verbose     : " + str(Globals.verbose));
    print_verbose("  start_path  : " + str(Globals.start_path));
    print_verbose("  output_path : " + str(Globals.output_path));
    print_verbose("  format      : " + str(Globals.output_format));
    print_verbose("  force       : " + str(Globals.force_conversion));
    print_verbose("");


################################################################################
## Run                                                                        ##
################################################################################
def run():
    #COWTODO: Check if start_path is valid.
    filenames = os.listdir(Globals.start_path);

    for filename in filenames:
        #Get the full filename of this file.
        input_full_filename = os.path.join(Globals.start_path, filename);

        #Not a file - ignore.
        if(not os.path.isfile(input_full_filename)): continue;
        #Hidden file - ignore.
        if(filename[0] == "."): continue;

        #Load the image...
        try:
            surface = pygame.image.load(os.path.abspath(input_full_filename));
        #If we cannot load the image, just log and ignore...
        except Exception, e:
            msg = "{} ({}) - {}".format(ColorError("Cannot load"),
                                        ColorPath(filename),
                                        str(e));
            print_error(msg);
            continue;


        #Create the output folder;
        folder_path = os.path.abspath(os.path.expanduser(Globals.output_path));
        try:
            os.makedirs(folder_path);
        except OSError, e:
            #Prevent the File Exists to be raised.
            if(e.errno != os.errno.EEXIST):
                e.filename = ColorPath(e.filename);
                print_fatal("Errno {} - {} - {}".format(e.errno,
                                                        e.strerror,
                                                        ColorPath(e.filename)));
        #Is Directory?
        if(not os.path.isdir(folder_path)):
            print_fatal("Output Dir Path is not a directory - ({})".format(
                        ColorPath(folder_path)));
        #Is Write enabled?
        if(not os.access(folder_path, os.W_OK)):
            print_fatal("Output Dir Path is not writable - ({})".format(
                        ColorPath(folder_path)));


        #Get the name end extension...
        input_name, input_ext = os.path.splitext(filename);
        input_ext = input_ext.replace(".", "");

        #Already on same format, don't need do anything else.
        #If --force is set DO NOT skip.
        if(input_ext == Globals.output_format and not Globals.force_conversion):
            msg = "{} ({}) - Same format".format(ColorInfo("Skipping:"),
                                                 ColorPath(filename));
            print_verbose(msg);
            continue;

        #Build the output filename
        output_filename      = input_name + "." + Globals.output_format;
        output_full_filename = os.path.join(Globals.output_path, output_filename);
        output_full_filename = os.path.abspath(os.path.expanduser(output_full_filename));

        #Already have a file with the target filename
        #If --force is set DO NOT skip.
        if(os.path.exists(output_full_filename) and not Globals.force_conversion):
            msg = "{} ({}) - {} ({})".format(ColorInfo("Skipping"),
                                             ColorPath(filename),
                                             "Output file already exists",
                                             ColorPath(output_filename));
            print_verbose(msg);
            continue;


        #Log.
        msg = "{} ({}) {} [{}] {} [{}]".format(ColorProcessing("Converting"),
                                               ColorPath(filename),
                                               ColorProcessing("from"),
                                               ColorInfo(input_ext),
                                               ColorProcessing("to"),
                                               ColorInfo(Globals.output_format));
        print_verbose(msg);


        #Try to save the output image.
        try:
            pygame.image.save(surface, output_full_filename);
            msg = "  {} ({})".format(ColorOK("Saved in"),
                                     ColorPath(output_full_filename));
            print_verbose(msg);

        #Log if anything goes wrong...
        except Exception, e:
            msg = "{} ({}) - {}".format(ColorError("Failed"),
                                          ColorPath(output_full_filename),
                                          str(e));
            print_error(msg);



################################################################################
## Script initialization                                                      ##
################################################################################
def main():
    #Get the options.
    try:
        options = getopt.gnu_getopt(sys.argv[1:],
                                    Constants.ALL_FLAGS_SHORT,
                                    Constants.ALL_FLAGS_LONG);
    except Exception, e:
        print_fatal(e);

    #Parse the flags.
    for option in options[0]:
        key, value = option;
        key = key.lstrip("-");

        #Help / Version / List - EXCLUSIVE
        if(key in Constants.FLAG_HELP        ): print_help   (0);
        if(key in Constants.FLAG_VERSION     ): print_version(0);
        if(key in Constants.FLAG_DISPLAY_EXT ): print_formats(0);

        #Verbose / Force - OPTIONALS
        if(key in Constants.FLAG_VERBOSE ): Globals.verbose = True;
        if(key in Constants.FLAG_FORCE   ): Globals.force_conversion = True;

        #Output Path / Output Format - OPTIONALS
        if(key in Constants.FLAG_OUTPUT_PATH   ): Globals.output_path   = value;
        if(key in Constants.FLAG_OUTPUT_FORMAT ): Globals.output_format = value;

        #No Colors - OPTIONALS
        if(key in Constants.FLAG_NO_COLORS):
            ColorMode.mode = ColorMode.NEVER;


    #Check if Output format is valid.
    if(Globals.output_format is None):
        Globals.output_format = Constants.SUPPORTED_FORMATS_PNG;

    #Lower the case - So users can type anything (Png PNG, pNg ...).
    Globals.output_format = Globals.output_format.lower();
    if(Globals.output_format not in Constants.SUPPORTED_FORMATS):
        print_formats();
        print_fatal("Invalid format: {}".format(Globals.output_format));
        exit(1);

    #Get the start path.
    if(len(options[1]) != 0):
        Globals.start_path = options[1][0];

    #Will print only in verbose mode.
    print_run_info();

    #Start...
    run();

if __name__ == '__main__':
    main();
