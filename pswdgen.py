# !/usr/bin/env python
# -*- coding: cp1250 -*-
# Author: Patryk Szczodrowski

import urllib.request
import random
import sys
import getopt
import os
import unicodedata
import tempfile

url = "http://www.math.uni.wroc.pl/~hebisch/prog/pol.lst"
numbers = [i for i in "1234567890"]
specialChars = [i for i in "!@#$%^&*?+="]

def remove_polish_characters(text):
    # Convert accented chars to their non-accented equivalent.
    # e.g.: żółć -> zolc
    normalized_text = unicodedata.normalize('NFD', text).encode('ascii', 'ignore').decode('utf-8')
    normalized_text = normalized_text.replace('ł', 'l').replace('Ł', 'L').replace('ą', 'a')\
        .replace('Ą', 'A').replace('ę', 'e').replace('Ę', 'E').replace('ó', 'o').replace('Ó', 'O')\
        .replace('ń', 'n').replace('Ń', 'N').replace('ć', 'c').replace('Ć', 'C').replace('ś', 's')\
        .replace('Ś', 'S').replace('ż', 'z').replace('Ż', 'Z').replace('ź', 'z').replace('Ź', 'Z')
    return normalized_text

def __readFile(linesFile):
    with open(linesFile, 'rb') as f:
        lines = f.readlines()
    return lines

def getLines(linesFile = F"{tempfile.gettempdir()}/pswdgen_lines.txt"):
    if os.path.exists(linesFile):
        lines = __readFile(linesFile)
    else:
        print("Downloading dictionary file. Please wait...")
        response = urllib.request.urlopen(url)
        with open(linesFile, 'wb') as f:
            f.write(response.read())
        lines = __readFile(linesFile)
    return lines

def getWords(count = 3, deacct = True):
    lines = getLines()
    words = [random.choice(lines).decode('cp1250').strip().split('/')[0].capitalize() for _ in range(count)]
    password = ''.join([str(elem) for elem in words])
    return(remove_polish_characters(password) if deacct else password)

def getNumbersAndSpecialChars(numCount = 2, specialCount = 1):
    postElement = [item for sublist in
        [[random.choice(numbers).strip() for _ in range(numCount)],
        [random.choice(specialChars).strip() for _ in range(specialCount)]] for item in sublist]
    return (''.join([str(elem) for elem in sorted(postElement, key=lambda k:random.random())]))

def printHelp():
    print("""
    pswdgen 0.1v 
    A program created for generating human-friendly passwords combined with words and special characters
    
    params:
    -c, --count: How many passwords should be generated
    -w, --words: How many words password should contain
    -n, --numbers: How many numbers should be in password
    -s, --specialchars: How many special characters should be in password
    -f, --file: File name to save output
    -h: Help
    """)
def printPassList(list):
    for index,el in enumerate(list):
        print(F"{index}: {el}")
def saveToFile(file, list):
    with open(file, 'w') as f:
        for index,el in enumerate(list):
            f.write(F"{index}: {el}\n")
if __name__ == "__main__":
    argv = sys.argv[1:]
    file = None
    try:
        opts, args = getopt.getopt(argv, "c:w:f:s:n:h",["count =","words =","file =","numbers =","specialchars ="])
    except:
        print("Brak parametrów")
        exit(1)
    for opt, arg in opts:
        if opt in ['-c', '--count']:
            count = int(arg)
        if opt in ['-w', '--words']:
            numberOfWords = int(arg)
        if opt in ['-f', '--file']:
            file = arg
        if opt in ['-n', '--numbers']:
            numCount = int(arg)
        else:
            numCount = 2
        if opt in ['-s', '--specialchars']:
            specialCount = int(arg)
        else:
            specialCount = 1
        if opt in ['-h']:
            printHelp()
            exit(0)
    try:
        passList = [
            [(getWords(numberOfWords)+(getNumbersAndSpecialChars(numCount,specialCount)))]
            for _ in range(count)
        ]
        if(file != None):
            saveToFile(file, passList)
        printPassList(passList)
    except(NameError):
        print("Enter parameters for generating passwords. -h for help.")