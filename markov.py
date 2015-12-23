#!/usr/bin/python2
#Create Dictionary
import random
from string import printable
frequency_list = {}
for letter in printable:
    frequency_list.update({letter:{}})
    for letter2 in printable:
        frequency_list[letter].update({letter2:0})

#open and scan file, filling dictionary
mobydick = open("mobydick.txt", "r");
first_char = "\n";
while True:
    second_char = mobydick.read(1);
    if not second_char:
        break;
    frequency_list[first_char][second_char] = frequency_list[first_char][second_char] + 1;
    first_char = second_char;

mobydick.close()


def weighted_choice(choices):
    total = sum(w for c, w in choices.iteritems())
    r = random.uniform(0, total)
    upto = 0
    for c, w in choices.iteritems():
        if upto + w >= r:
            return c
        upto += w
    assert False, "mess up"

#generate a string of text
num = 0
output = ""
next_char = "a"
while num < 500:
    next_char =  weighted_choice(frequency_list[next_char]);
    output = output + next_char;
    num = num + 1;

print output;
