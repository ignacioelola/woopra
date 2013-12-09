import requests
import json
import datetime
import os
import sys


def visit(email,date):
    endpoint = "http://www.woopra.com/rest/profile/visits"
    headers= {'X-Api-Version':"2.0",
          'X-Access-Id':your_access_id,
         'X-Access-Secret': your_access_secret}

    data = {"website": your_website,
        "email": email,
        "latest": "false",
        "to": date,
        "date_format": "dd-MM-yyyy",
        "limit": 500}

    print "Searching visits..."     
    r = requests.post(endpoint, data={"request": json.dumps(data)}, headers=headers)
    try:
      response=r.json()
    except:
      print r
      response=False
    return response



def profile(email):
    endpoint = "http://www.woopra.com/rest/profile"
    headers= {'X-Api-Version':"2.0",
          'X-Access-Id':your_access_id,
         'X-Access-Secret': your_access_secret}

    data = {"website": your_website,
        "email": email,
        "date_format": "dd/MM/yyyy"}

    print "Searching profile..." 
    r = requests.post(endpoint, data={"request": json.dumps(data)}, headers=headers)
    try:
      response=r.json()
    except:
      print r
      response=False
    return response



def profile_pid(pid):
    endpoint = "http://www.woopra.com/rest/profile"
    headers= {'X-Api-Version':"2.0",
          'X-Access-Id':your_access_id,
         'X-Access-Secret': your_access_secret}
    
    data = {"website": your_website,
        "pid": pid,
        "date_format": "dd/MM/yyyy"}  

    print "Searching profile..." 
    r = requests.post(endpoint, data={"request": json.dumps(data)}, headers=headers)
    try:
      response=r.json()
    except:
      print r
      response=False
    return response


def search_pageview(start_date,end_date,pageview):

    woopra_endpoint = "http://www.woopra.com/rest/search"
    headers= {'X-Api-Version':"2.0",
          'X-Access-Id':your_access_id,
         'X-Access-Secret': your_access_secret}

    woopra_data = {"website": your_website,
        "limit": 10000,
        "offset": 0,
        "date_format": "yyyy-MM-dd",
        "start_day": start_date,
        "end_day": end_date,
        "segments": [{"are": {
                              "operator" : "AND",
                              "filters": [                
                                         ]},
                      "did": {
                              "operator" : "AND",
                              "filters": [ {
                                            "action":{ "operator": "AND",
                                                      "filters": [{
                                                                  "_uikey": "pv:url",
                                                                  "scope": "actions",
                                                                  "key": "url",
                                                                  "match": "contains",
                                                                  "value": pageview
                                                                   }]},
                                          "aggregation":{
                                                         "method": "count",
                                                         "scope": "visits", 
                                                         "match": "gte",
                                                         "value": 1
                                                          },
                                          "timeframe":{
                                                           "method": "absolute",
                                                           "from": start_date,
                                                           "to": end_date
                                                       },
                                            "visit":{
                                                     "operator": "AND",
                                                     "filters": []}
                                            }]}
                      }],
        "report_id": -1}

    print "Searching %s..." % pageview
    r = requests.post(woopra_endpoint, data={"request": json.dumps(woopra_data)}, headers=woopra_headers)
    woopra_response_=r.json()
    woopra_response=woopra_response_["visitors"]

    if len(woopra_response)!= woopra_response_["total"]:
        return "not all data is coming back, total results should be %s" % r.json["total"]   

    return woopra_response








