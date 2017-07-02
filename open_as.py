# /usr/local/bin/python3
# -*- coding: utf8 -*-

import os, random, argparse, webbrowser

parser = argparse.ArgumentParser()
parser.add_argument('-r', '--radio_only', dest = 'radio_only', action = 'store_true', default = False)
args = parser.parse_args()

def choose(f):
    f = open(f, encoding='utf8').read().split('\n')
    c = random.choice(f)
    return c

def runAppleScript(f, delay, *args):
    f = open(f, encoding='utf8').read()
    f = f%(radio, weather, traffic, delay)
    os.system("osascript -e '%s'"%f)

if __name__ == '__main__':

    cwd = os.path.dirname(os.path.realpath(__file__))
    radio = choose(cwd+'/radio.txt')

    if args.radio_only:
        print('radio_only')
        webbrowser.open(radio)
    else:
        weather = choose(cwd+'/weather.txt')
        traffic = choose(cwd+'/traffic.txt')
        runAppleScript(cwd+'/applescript_budilnick.txt', 600, radio, weather, traffic)