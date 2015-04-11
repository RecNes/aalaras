#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys, getopt, random


class Main():
    def __init__(self, argv):
        self.infile = ""
        self.destdir = ""
        self.counter = 0
        self.search_text = 'alt=""'
        self.source_file_content = str()
        self.temp_content = str()
        self.word_list = list()
        self.word_count = int()
        self.file_list = list()
        self.argv = argv

    def get_args(self):
        """
        This tool does scan destination diretory for html files and assigns 
        random word from given keywords in the source file to the empty "alt" 
        argument in <img> tags. Keywords are must be comma seperated without
        newline.

        Usage:
                aalaras.py -i <inputfile> -d <destdir>

                -i, --ifile      File that contains keywords splitted with commas
                -d, --destdir    Destination directory where html files exist
                
        USE AT YOUR OWN RISK: This script is working good enough for me. But, script
        may destroy your files. You must do a backup before using this script.
        
        Feel free to modify this script as your requirements. Do not forget to 
        script be able to modify just ascii or unicode text type files. Binary 
        files are out of question.

        aalaras by Sencer Hamarat (http://www.recnes.com/) 2015
        """
        if not len(self.argv) > 1:
            print "No arguments given. -h for help"
            sys.exit(2)
        try:
            opts, args = getopt.getopt(self.argv[1:], "hi:d:", ["ifile=", "destdir="])
        except getopt.GetoptError:
            print 'Error in arguments'
            sys.exit(2)
        for opt, arg in opts:
            if opt == '-h':
                print self.get_args.__doc__
                sys.exit()
            elif opt in ("-i", "--ifile"):
                self.infile = arg
                if self.infile == "-d":
                    print "Input file argument is invalid"
                    sys.exit(2)
            elif opt in ("-d", "--destdir"):
                self.destdir = arg

    def read_file(self, state="full"):
        try:
            if state == "full":
                with open(self.infile, "r") as infile:
                    self.source_file_content = infile.read()
            elif state == "line":
                with open(self.infile, "r") as infile:
                    self.source_file_content = infile.readlines()
        except IOError:
            print "No such file '%s' available" % self.infile
            sys.exit(2)

    def make_word_list(self):
        self.read_file()
        self.word_list = self.source_file_content.replace("\n", "").split(",")
        if not len(self.word_list) > 0:
            print "'%s' file has no content"
            sys.exit(2)
        self.word_count = len(self.word_list)
        print "%s word%s counted" % (self.word_count, 's' if self.word_count > 1 else '')

    def get_a_word(self):
        word = 'alt="%s"' % random.choice(self.word_list).strip()
        self.counter += 1
        if self.counter > (self.word_count - 1):
            self.counter = 0
        return word

    def find_files(self):
        for root, dirs, files in os.walk(self.destdir):
            for f in files:
                if f.endswith(".html"):
                    self.file_list.append(os.path.join(root, f))
        print "%s file%s found" % (len(self.file_list), 's' if len(self.file_list) > 1 else '')

    def write_file(self, result):
        try:
            with open(self.infile, "w") as outfile:
                outfile.write(result)
            print "%s file modified" % self.infile
        except IOError:
            print "Error while writing '%s' file" % self.infile
            sys.exit(2)

    def find_replace(self):
        print "-" * 80
        print "STATUS:"
        self.get_args()
        self.make_word_list()
        self.find_files()
        print "-" * 80
        print ""
        print "RESULTS:"
        print "-" * 80
        for self.infile in self.file_list:
            self.temp_content = ""
            self.read_file(state="line")
            for line in self.source_file_content:
                if self.search_text in line:
                    line = line.replace(self.search_text, self.get_a_word())
                self.temp_content += line
            self.write_file(self.temp_content)
        print "-" * 80

if __name__ == "__main__":
    print "Automatic Alt Argument Assigner"
    Main(sys.argv).find_replace()
    sys.exit()
