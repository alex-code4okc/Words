import argparse
import re
from collections import Counter

# give match_string global scope
match_string = ''
file_s = ''
words = ''

parser = argparse.ArgumentParser(description='Count the word or letter frequencies found in a txt file.')

command_group = parser.add_mutually_exclusive_group()
command_group.add_argument('-w',help='Count the frequency of words found in the file.',action= 'store_true')
command_group.add_argument('-l',help='Count the frequency of letters found in the file.', action='store_true')

parser.add_argument('-i','--input',help='The name of the file to be used as input.',required=True)

parser.add_argument('-o','--output',help='The name of the output file.')

args = parser.parse_args()

with open(args.input) as input_file:
    if(args.w):
        # one or more alphanumeric characters
        match_string = r'\w+'
    elif (args.l):
        # anything that is not a number
        match_string = '[^0-9]'
    else:
        # one or more alphanumeric characters (the default if no -w or -l argument specified)
        match_string = r'\w+'

    file_s = input_file.read() 
    # do not treat lower case and upper case as different words
    file_s=file_s.upper() 
    words = re.findall(match_string, file_s, re.I | re.A) 
    words_counter = Counter(words)

with open(args.output,'w') as output_file:
    for key,value in words_counter.most_common():
        print(key,value,sep=':',file=output_file)