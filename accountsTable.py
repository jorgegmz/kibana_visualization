#!/usr/bin/python
import sys
import numpy as np
import pandas as pd
# import ijson
import json
from bs4 import BeautifulSoup


def vizJSON(ky, dic):

    val = {
    "_id": ky+"-95th-Percentile-time-taken",
    "_type": "visualization",
    "_source": {
      "title": ky+" - 95th Percentile time-taken",
      "visState": "{\"title\":\""+ky+" - 95th Percentile time-taken\",\"type\":\"line\",\"params\":{\"shareYAxis\":true,\"addTooltip\":true,\"addLegend\":true,\"showCircles\":true,\"smoothLines\":true,\"interpolate\":\"linear\",\"scale\":\"linear\",\"drawLinesBetweenPoints\":true,\"radiusRatio\":9,\"times\":[],\"addTimeMarker\":false,\"defaultYExtents\":false,\"setYExtents\":false,\"yAxis\":{},\"grid\":{\"categoryLines\":false,\"style\":{\"color\":\"#eee\"}},\"categoryAxes\":[{\"id\":\"CategoryAxis-1\",\"type\":\"category\",\"position\":\"bottom\",\"show\":true,\"style\":{},\"scale\":{\"type\":\"linear\"},\"labels\":{\"show\":true,\"truncate\":100},\"title\":{\"text\":\"@timestamp per 30 seconds\"}}],\"valueAxes\":[{\"id\":\"ValueAxis-1\",\"name\":\"LeftAxis-1\",\"type\":\"value\",\"position\":\"left\",\"show\":true,\"style\":{},\"scale\":{\"type\":\"linear\",\"mode\":\"normal\",\"setYExtents\":false,\"defaultYExtents\":false},\"labels\":{\"show\":true,\"rotate\":0,\"filter\":false,\"truncate\":100},\"title\":{\"text\":\"Percentiles of time-taken\"}}],\"seriesParams\":[{\"show\":\"true\",\"type\":\"line\",\"mode\":\"normal\",\"data\":{\"label\":\"Percentiles of time-taken\",\"id\":\"1\"},\"valueAxis\":\"ValueAxis-1\",\"drawLinesBetweenPoints\":true,\"showCircles\":true,\"interpolate\":\"cardinal\",\"radiusRatio\":9}],\"legendPosition\":\"right\",\"type\":\"line\"},\"aggs\":[{\"id\":\"1\",\"enabled\":true,\"type\":\"percentiles\",\"schema\":\"metric\",\"params\":{\"field\":\"time-taken\",\"percents\":[95]}},{\"id\":\"2\",\"enabled\":true,\"type\":\"date_histogram\",\"schema\":\"segment\",\"params\":{\"field\":\"@timestamp\",\"interval\":\"auto\",\"customInterval\":\"2h\",\"min_doc_count\":1,\"extended_bounds\":{}}},{\"id\":\"3\",\"enabled\":true,\"type\":\"filters\",\"schema\":\"group\",\"params\":{\"filters\":[{\"input\":{\"query\":{\"query_string\":{\"query\":\"appid: "+dic[ky]+"\",\"analyze_wildcard\":false}}},\"label\":\""+ky+"\"}]}}],\"listeners\":{}}",
      "uiStateJSON": "{}",
      "description": "",
      "version": 1,
      "kibanaSavedObjectMeta": {
        "searchSourceJSON": "{\"index\":\"AWBcepPXMhxNtLqjCPxV\",\"query\":{\"query_string\":{\"query\":\"(appid: "+dic[ky]+")\",\"analyze_wildcard\":false}},\"filter\":[]}"
      }
    }
    }
    """
    filename = "visualization_shell.json"
    f = open(filename, "r")
    json_object = json.load(f)
    # replace _id
    json_object[0]["_id"] = json_object[0]["_id"].replace("-95th-Percentile-time-taken",
                                                          ky + "-95th-Percentile-time-taken")
    # print("val: {}".format(json_object[0]["_id"]))

    # replace title
    json_object[0]["_source"]["title"] = json_object[0]["_source"]["title"].replace(" - 95th Percentile time-taken",
                                                                                    ky + " - 95th Percentile time-taken")
    # print("val: {}".format(json_object[0]["_source"]["title"]))

    # replace visState title
    json_object[0]["_source"]["visState"] = json_object[0]["_source"]["visState"].replace(
        " - 95th Percentile time-taken", (ky + " - 95th Percentile time-taken"))
    # print("val: {}".format(json_object[0]["_source"]["visState"]))

    # replace visState appid
    json_object[0]["_source"]["visState"] = json_object[0]["_source"]["visState"].replace("appid: ", "appid: " + dic[ky])
    # print("val: {}".format(json_object[0]["_source"]["visState"]))

    # replace visState accid
    json_object[0]["_source"]["visState"] = json_object[0]["_source"]["visState"].replace("}]}}]", ky + "}]}}]")
    # print("val: {}".format(json_object[0]["_source"]["visState"]))

    json_object[0]["_source"]["kibanaSavedObjectMeta"]["searchSourceJSON"] = json_object[0]["_source"]["kibanaSavedObjectMeta"]["searchSourceJSON"].replace("(appid: )", "(appid: " + dic[ky] + ")")    # print(json_object[0]["_source"]["kibanaSavedObjectMeta"])

    # print("val: {}".format(json_object))
    f.close()
    # json_object+=json_object+","
    return json.dumps(json_object)
    """
    return val

def parseTable(textToRead):
    f = open(textToRead)
    soup = BeautifulSoup(f, 'html.parser')
    f.close()
    count = 0
    file = []
    myDict = dict()
    for row in soup.tbody:
        for r in row:
            count += 1
            if count == 3:
                key = ''.join(r)
            elif count == 9:
                val = ''.join(str(x) for x in r)
                myDict[key] = val
                # print("before function call")
                file.append(vizJSON(key, myDict))# += str(vizJSON(key, myDict))+","
                # print("just called function")
            if count == 11:
                count = 0
    # file = file.rstrip(',')+"]"
    return json.dumps(file)



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
        # print(json.dumps(printDict))
        print(printDict)
        # print("len: {}".format(len(printDict)))
        # print(printDict)
        # for k in printDict:
        #     print("{}".format(k))

if __name__ == '__main__':
    main()
