#!/usr/bin/python
import sys
from bs4 import BeautifulSoup

def parseTable(textToRead):
    f = open(textToRead)
    soup = BeautifulSoup(f, 'html.parser')
    f.close()
    #print(soup)
    count = 0
    myDict = dict()
    for row in soup.tbody:
        for r in row:
            count += 1
            if count == 3:
                key = ''.join(r)
                #key = str(r).split("<td>")
                #key = key[1].split("</td>")
                #key = ''.join(key)
            elif count == 9:
                #val = str(r).split("<td>")
                #val = val[1].split("</td>")
                #val = str(val)
                val = ''.join(str(x) for x in r)
                myDict[key] = val.split()
                #print("key: {} val: {}".format(key, myDict[key]))
            if count == 11:
                count = 0
    return myDict
            #print("type: {} val: {}".format(type(r), r))
            #count += 1
            #if count == 3 or count == 9:
             #   print(len(r))
              #  print(r)
               # print("row type: {} row len: {} row val: {}".format(type(r), len(r), r))
            #if count == 10:
             #   count = 0

   # for row in open(textToRead, "r"):
    #    row = row.split("<td></td>")
     #   print("row type: {} row len: {} row val: {}".format(type(row), len(row), row))
        #tm = list(tmp)
        #row = ''.join(c for c in row if c not in '<>/trtd')
        #print("tmp length: {} tmp type: {} tmp idx: {} tmp value: {}".format(len(tm), type(tm), tm[0], tm))
            #print("accoID {}".format(row))
        #print(row)
        #print(type(row))
            #temp = row.split("AccountID")
            #print(temp)
       # print(row)




    #for title in soup.find_all("tr"):
     #   row = title.find_all("td")
      #  print("td {}".format(row))
        #accID = row
        #appID = row[7]
        #print("acountID {} appID".format(accID, appID))
    #title = soup.find_all(enumerate("th"))
    #print(title)
    #with BeautifulSoup(codecs.open(textToRead, "html.parser")) as f:
     #   for line in f.findAll('tr')[2::8]:
      #      print(line)



#for k, v in printDict.items():
 #   print("key: {} val: {}" .format(k,v))
def read_in():
   return [x.strip() for x in sys.stdin.readlines()]


def main():
    while True:
        #print(sys.argv)
        #print(len(sys.argv))
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
        #break

    #printDict = parseTable(args[1])
    #for k,v in printDict.items():
     #   print("{} {}".format(k, printDict[k]))

    #print(sys.argv[1])
   # with open(sys.argv[1], 'r') as fin, open(sys.argv[2], 'r') as fout:
    #    printDict = parseTable(fin)
     #   for k,v in printDict.items():
      #      print("{} {}".format(k, printDict[k]))
    #string = "production_database_servers.html"
    ##printDict = parseTable(string)
    ##for k,v in printDict.items():
       ## print("{} {}".format(k, printDict[k]))

if __name__ == '__main__':
    main()
