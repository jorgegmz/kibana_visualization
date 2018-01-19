#!/usr/bin/python
import sys
import numpy as np
import pandas as pd
import ijson
from bs4 import BeautifulSoup


def vizJSON(ky, dic):

    #for t in f:
     #   t = t.strip().split()
    #    if t[0] == "_id":
     #       t[1] = ky.append(t[1])
      #      print("id: {}".format(t[1]))
       # elif t[0] == "title":
        #    t[2] = ky + t[2]
         #   print("title: {}".format(t[2]))
    #    elif t[0] == "visState":
     #       t[2] = ky + t[2]
      #      print("Last value {}".format(t[13]))
       # elif t[0] == "searchSourceJSON":
        #    print("Find idx {}".format(t[1]))
      #  print("type: {} rowlen {} reading each row: {}".format(type(t), len(t), t))
    return ""


def parseTable(textToRead):
    f = open(textToRead)
    soup = BeautifulSoup(f, 'html.parser')
    f.close()
    count = 0
    file = ""
    myDict = dict()
    for row in soup.tbody:
        for r in row:
            count += 1
            if count == 3:
                key = ''.join(r)
            elif count == 9:
                val = ''.join(str(x) for x in r)
                myDict[key] = val
                file += (vizJSON(key, myDict))
            if count == 11:
                count = 0
    return myDict



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
