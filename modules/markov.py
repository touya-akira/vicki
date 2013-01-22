#!/usr/bin/python

import time
import os
from collections import defaultdict

debugchan = '#akirav'
initialized = False
markov = defaultdict(list)
chain_length = 2
chattiness=0.05
STOP_WORD = "\n"

def add_to_brain(phenny, input):
    f = open('training_text.txt', 'a')
    f.write(input.group() + '\n')
    f.close()
    buf = [STOP_WORD] * chain_length
    for word in input.group().split():
        markov[tuple(buf)].append(word)
        del buf[0]
        buf.append(word)
    markov[tuple(buf)].append(STOP_WORD)
add_to_brain.event = 'PRIVMSG'
add_to_brain.rule = r'.*'
add_to_brain.priority = 'medium'

def reload_brain(msg, chain_length=2):
    buf = [STOP_WORD] * chain_length
    for word in msg.split():
        markov[tuple(buf)].append(word)
        del buf[0]
        buf.append(word)
    markov[tuple(buf)].append(STOP_WORD)

#def mminit(phenny, input):
f = open('training_text.txt', 'r+')
for line in f:
   	reload_brain(line, chain_length)
#phenny.say('Brain Reloaded')
f.close()
#mminit.commands = ['minit']


