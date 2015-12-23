#!/usr/bin/python2
#Create Dictionary
import random, sys
from string import ascii_lowercase
from string import ascii_letters
word_list = {}

def get_next_word(text):
    word = "";
    char = text.read(1);
    if(not char):
        return word;
    while(ascii_letters.find(char) == -1):
        char = text.read(1);
    while(ascii_letters.find(char) != -1 and char):
        word += char;
        char = text.read(1);
    return word.lower();


def weighted_choice(choices):
    total = sum(w for c, w in choices.iteritems())
    r = random.uniform(0, total)
    upto = 0
    for c, w in choices.iteritems():
        if upto + w >= r:
            return c
        upto += w
    assert False, "mess up"

#open and scan file, filling dictionary
input_text = open(sys.argv[1], "r");
first_word = get_next_word(input_text);

while True:
    second_word = get_next_word(input_text);
    if(second_word == ""):
        break;
    if(not word_list.has_key(first_word)):
        word_list.update({first_word:{}});
    if(not word_list[first_word].has_key(second_word)):
        word_list[first_word].update({second_word:0});
    else:
        word_list[first_word][second_word] += 1;

    first_word = second_word;

input_text.close()

print str(word_list);

#generate a string of text
num = 0
output = ""
next_word = "a"
while num < 500:
    next_word =  weighted_choice(word_list[next_word]);
    output += " " + next_word;
    num = num + 1;

print output;
