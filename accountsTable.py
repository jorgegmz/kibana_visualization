#!/usr/bin/python
import sys
from bs4 import BeautifulSoup

def parseTable(textToRead):
    f = open(textToRead)
    soup = BeautifulSoup(f, 'html.parser')
    f.close()
    count = 0
    myDict = dict()
    for row in soup.tbody:
        for r in row:
            count += 1
            if count == 3:
                key = ''.join(r)
            elif count == 9:
                val = ''.join(str(x) for x in r)
                myDict[key] = val.split()
            if count == 11:
                count = 0
    return myDict

def read_in():
   return [x.strip() for x in sys.stdin.readlines()]


def main():
    while True:
        try:
            if len(sys.argv) == 1:
                args = input("Enter file name: ")
                break
            else:
                args = sys.argv[1]
                break
        except ValueError:
            print("Has to be a valid file")
            continue
    if len(args) > 0:
        printDict = parseTable(args)
        for k,v in printDict.items():
            print("{} {}".format(k, printDict[k]))

if __name__ == '__main__':
    main()
