# /usr/local/bin/python3
# -*- coding: utf8 -*-

import os, random

def choose(f):
    f = open(f, encoding='utf8').read().split('\n')
    c = random.choice(f)
    return c

def runAppleScript(f, *args):
    f = open(f, encoding='utf8').read()
    f = f%(radio, traffic, weather)
    os.system("osascript -e '%s'"%f)

if __name__ == '__main__':

    cwd = os.path.dirname(os.path.realpath(__file__))

    radio = choose(cwd+'/radio.txt')
    traffic = choose(cwd+'/traffic.txt')
    weather = choose(cwd+'/weather.txt')
    runAppleScript(cwd+'/applescript_budilnick.txt', radio, weather, traffic)