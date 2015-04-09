# aalaras
## Automatic Alt Argument Assigner

# Description:
This tool does scan destination diretory for html files and assigns 
random word from given keywords in the source file to the empty "alt" 
argument in <img> tags. Keywords are must be comma seperated without
newline.

# Usage:
        
        # ./aalaras.py -i <inputfile> -d <destdir>

        -i, --ifile      File that contains keywords splitted with commas
        -d, --destdir    Destination directory where html files exist
        
# USE AT YOUR OWN RISK: 
This script is working good enough for me. But, script may destroy your 
files. You must do a backup before using this script.

Feel free to modify this script as your requirements. Do not forget to 
script be able to modify just ascii or unicode text type files. Binary 
files are out of question.

# Requirements:

Python (2.6+) must be installed in your system.

## aalaras by Sencer Hamarat (http://www.recnes.com/) 2015
