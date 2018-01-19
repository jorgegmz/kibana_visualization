#!/usr/bin/python
import sys
import pprint
import ijson
from bs4 import BeautifulSoup


def beRightBack():
    filename = "visualization_shell.json"
    f = open(filename, 'r')
    accID = "AdidasGlobal"
    appID = "adidasmobglobal adidaswebar adidaswebau adidaswebat adidaswebbe adidaswebbr adidaswebca adidaswebcl adidaswebco adidaswebcz adidaswebdk adidaswebfi adidaswebfr adidaswebde adidaswebie adidaswebit adidaswebmx adidaswebnl adidaswebnz adidaswebpe adidaswebpl adidaswebru adidaswebsk adidaswebes adidaswebse adidaswebuk adidasuk adidaswebjp adidasmobjp testid AdidasGlobal01 adidaswebch adidaswebmy adidaswebph adidaswebpt adidaswebgr adidaswebno"
    count = 0
    fileToReturn = []
    for row in f:
        #print(row)
        #fileToReturn.append(row)
        #print(fileToReturn)
        count += 1
        if count == 3:
            _id = row.strip().split(":")
            accountID = accID
            accountID += _id[1]
            _id[1] = accountID.replace(" ", "") #prepending accID to string
            fileToReturn.append(_id[1])
            #print("count: {} type: {} row: {}".format(count, type(_id), _id[1]))
        elif count == 6:
            title = row.strip().split(":")
            accountTitle = accID
            accountTitle += title[1]
            title[1] = accountTitle #prepending accID to string
            fileToReturn.append(title[1])
            #print("count {} row: {}".format(count, title[1])) #key insert. append
        elif count == 7:
            visState = row.strip().split(":")
            visStateTitle = accID
            visStateTitle += visState[2]
            visState[2] = visStateTitle #prepending accID to string
            fileToReturn.append(visState[2])
            #print("count: {} type {} row: {}".format(count, type(visState[2]), visState[2])) #key insert before 95th percentile. append
            visStateAppID = appID
            visState[96] += " : " + visStateAppID #append appID to string
            fileToReturn.append(visState[96])
            #print("count: {} row: {}".format(count, visState[96])) #appID insert.Last element in list. This will involve an append
            visStateLabel = accID
            visState[98] += " : " + visStateLabel #append appID to string
            fileToReturn.append(visState[98])
            #print("count: {} row: {}".format(count, visState[98]))#key insert after "label: "
        elif count == 12:
            searchSourceJSON = row.strip().split(":")
            searchSourceJSONAppID = appID
            searchSourceJSON[5] += ": " + searchSourceJSONAppID #append appID to string
            fileToReturn.append(searchSourceJSON[5])
            #print("count: {} row: {}".format(count, searchSourceJSON[5]))
    f.close()
    return fileToReturn


print(beRightBack())