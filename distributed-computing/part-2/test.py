import requests as r
import threading

cities = ["baltimore", "charleston", "chicago", "columbus", "dayton",
          "denver", "kc", "memphis", "milwaukee", "ok_city", "pittsburgh",
          "st_louis", "syracuse", "wichita"]

url = "http://sample-env.nzpc2rmevt.us-west-2.elasticbeanstalk.com/"

def get_avg(c):
    res = r.get(str(url) + '/average_pop?city=' + c)
    print(c + " average population: " + res.text)

for c in cities:
    threading.Thread(target=get_avg, args=(c,)).start()
