#!/usr/bin/python3
#
# Run this from the same directory as the folder containing data
# python3 wordlist.py -i languages/marra
#    .
#    |----   marra
#    |    |---- sounds
#    |    |    |---- word1.wav
#    |    |    |---- word2.wav
#    |    |---- translations
#    |    |    |---- word1.txt
#    |    |    |---- word2.txt
#    |    |---- words
#    |         |---- word1.txt
#    |         |---- word2.txt
#    |---- wordlist.py

import argparse
import glob
import os


parser = argparse.ArgumentParser(description='Groups word text with corresponding translation text from separate files, saves as a dict.txt file')
parser.add_argument('-i', '--input_dir', help='The input data dir', type=str, default="marra", required=True)
args = parser.parse_args()
input_dir = args.input_dir


def find_files_by_ext(set_of_all_files, exts):
    res = []
    for f in set_of_all_files:
        name, ext = os.path.splitext(f)
        if ("*" + ext.lower()) in exts:
            res.append(f)
    return res


def read_translation(file_name):
    in_dir, name = os.path.split(file_name)
    trans_file_name = os.path.join(input_dir, "translations", name)
    with open(trans_file_name, 'r') as f:
        translation = f.read()
        f.close()
        return translation


def read_file(file_name):
    with open(file_name, 'r') as f:
        word = f.read()
        f.close()
    translation = read_translation(file_name)
    return word, translation


g_exts = ["*.txt"]
all_word_files_in_dir = glob.glob(os.path.join(input_dir, "words", "**"))
word_file_names = find_files_by_ext(set(all_word_files_in_dir), set(g_exts))

with open(os.path.join(input_dir, 'dict.txt'), 'w') as fw:
    for file_name in word_file_names:
        word, trans = read_file(file_name)
        fw.write("%s\t%s\n" % (word, trans))
fw.close()
