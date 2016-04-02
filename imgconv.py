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
##        and must notbe misrepresented as being the original software.       ##
##     4. This notice may not be removed or altered from any source           ##
##        distribution.                                                       ##
##     5. Most important, you must have fun. ;)                               ##
##                                                                            ##
##      Visit opensource.amazingcow.com for more open-source projects.        ##
##                                                                            ##
##                                  Enjoy :)                                  ##
##----------------------------------------------------------------------------##


## Imports ##
import os;
import os.path;
import sys;
import getopt;
import pygame.image;

import pdb;

################################################################################
## Globals                                                                    ##
################################################################################
class Globals:
    verbose     = False;

    start_path  = ".";
    output_path = "./imgconv_output";

    output_ext  = "png";

    force_conversion = False;

################################################################################
## Constants                                                                  ##
################################################################################
class Constants:
    ##Flags
    FLAG_HELP        = "h", "help";
    FLAG_VERSION     = "v", "version";
    FLAG_DISPLAY_EXT = "L", "list-formats";

    FLAG_VERBOSE     = "V", "verbose";

    FLAG_OUTPUT_PATH = "o", "output";
    FLAG_OUTPUT_EXT  = "f", "format";

    FLAG_FORCE       = "force";


    ALL_FLAGS_SHORT = "hvLVo:f:";
    ALL_FLAGS_LONG  = ["help",
                       "version",
                       "list-formats",
                       "verbose",
                       "output=",
                       "format=",
                       "force"];

    SUPPORTED_FORMATS      = ["bmp", "tga", "png", "jpg", "jpeg"];
    SUPPORTED_FORMATS_BMP  = SUPPORTED_FORMATS[0];
    SUPPORTED_FORMATS_TGA  = SUPPORTED_FORMATS[1];
    SUPPORTED_FORMATS_PNG  = SUPPORTED_FORMATS[2];
    SUPPORTED_FORMATS_JPG  = SUPPORTED_FORMATS[3];
    SUPPORTED_FORMATS_JPEG = SUPPORTED_FORMATS[4];

    #App
    APP_NAME      = "imgconv";
    APP_VERSION   = "0.1.0";
    APP_AUTHOR    = "N2OMatt <n2omatt@amazingcow.com>"
    APP_COPYRIGHT = "\n".join(("Copyright (c) 2016 - Amazing Cow",
                               "This is a free software (GPLv3) - Share/Hack it",
                               "Check opensource.amazingcow.com for more :)"));

################################################################################
## Print Functions                                                            ##
################################################################################
def print_verbose(msg):
    if(Globals.verbose):
        print msg;

def print_fatal(msg):
    print "[FATAL]", msg;
    exit(1);


def print_help():
    msg = "Usage:" + """
  """;
    print msg;

def print_version():
    print "{} - {} - {}".format(Constants.APP_NAME,
                                Constants.APP_VERSION,
                                Constants.APP_AUTHOR);
    print Constants.APP_COPYRIGHT;
    print;

def print_formats():
    print "{} - {} - {}".format(Constants.APP_NAME,
                                Constants.APP_VERSION,
                                "AmazingCow");

    print "Output formarts supported: ";
    print "   " + " - ".join(Constants.SUPPORTED_FORMATS);


def print_run_info():
    print_verbose("Run info");
    print_verbose("  verbose     : " + str(Globals.verbose));
    print_verbose("  start_path  : " + str(Globals.start_path));
    print_verbose("  output_path : " + str(Globals.output_path));
    print_verbose("  format      : " + str(Globals.output_ext));
    print_verbose("  force       : " + str(Globals.force_conversion));
    print_verbose("");


################################################################################
## Run                                                                        ##
################################################################################
def run():
    filenames = os.listdir(Globals.start_path);
    # pdb.set_trace();

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
            msg = "Skipping {} - {}".format(filename, str(e));
            print_verbose(msg);
            continue;

        #Create the output folder;
        folder_path = os.path.abspath(os.path.expanduser(Globals.output_path));
        os.system("mkdir -p {}".format(folder_path));

        #Get the name end extension...
        input_name, input_ext = os.path.splitext(filename);
        input_ext = input_ext.replace(".", "");

        #Already on same format, don't need do anything else.
        if(input_ext == Globals.output_ext):
            msg = "Skipping {} - Same format".format(filename);
            print_verbose(msg);
            continue;

        #Build the output filename
        output_filename      = input_name + "." + Globals.output_ext;
        output_full_filename = os.path.join(Globals.output_path, output_filename);


        #Already have a file with the target filename - Just continue on --force
        if(os.path.exists(output_full_filename) and not Globals.force_conversion):
            msg = "Skipping {} - Output file already exists ({})".format(filename,
                                                                         output_filename);
            print_verbose(msg);
            continue;


        #Log.
        msg = "Coverting {} from ({}) to ({})".format(filename,
                                                      input_ext,
                                                      Globals.output_ext);
        print_verbose(msg);

        #Try to save the output image.
        try:
            pygame.image.save(surface, output_full_filename);
            msg = "  Saved in {}".format(output_full_filename);
            print_verbose(msg);
        #Log if anything goes wrong...
        except Exception, e:
            msg = "  Failed {}".format(output_full_filename);
            print_verbose(msg);
            print_verbose(str(e));



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

        #Help and Version Flags.
        if(key in Constants.FLAG_HELP):
            print_help();
            exit(0);
        if(key in Constants.FLAG_VERSION):
            print_version();
            exit(0);
        if(key in Constants.FLAG_DISPLAY_EXT):
            print_formats();
            exit(0);

        #Verbose Flag.
        if(key in Constants.FLAG_VERBOSE):
            Globals.verbose = True;

        #Verbose Flag.
        if(key == Constants.FLAG_FORCE):
            Globals.force_conversion = True;

        #Output Path Flag.
        if(key in Constants.FLAG_OUTPUT_PATH):
            Globals.output_path = value;
        #Output Ext Flag.
        if(key in Constants.FLAG_OUTPUT_EXT):
            Globals.output_ext = value;

    #Check if Output format is valid.
    if(Globals.output_ext is None):
        Globals.output_ext = Constants.SUPPORTED_FORMATS_PNG;

    Globals.output_ext = Globals.output_ext.lower();
    if(Globals.output_ext not in Constants.SUPPORTED_FORMATS):
        print_formats();
        print_fatal("Invalid format: {}".format(Globals.output_ext));
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
