from urllib.request import urlopen, Request
import requests, re
from bs4 import BeautifulSoup



#my urlopen
def my_urlopen(url):
    headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
               "Accept-Encoding": "gzip, deflate, br",
               "Accpet-Language": "zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7,ja;q=0.6,ar;q=0.5",
               "Cache-Control": "max-age=0",
               "Conncetion":"keep-alive",
               "Cookie": "",
#               "Host": "bugzilla.kernel.org",
               "Upgrade-Insecure-Requests": "1",
                "DNT": "1",
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}

    session = requests.Session()
    req = session.get(url, headers=headers)
    bspage = BeautifulSoup(req.text,"xml")		
    return bspage


def bug_template(bs_obj,project):
    [s.extract() for s in bs_obj('attachment')] 
#    print(bs_obj)
    bug_id = bs_obj.find("bug_id").get_text()
    bt = open("./data/" + project + "_" + bug_id + ".xml", "w")
    bt.write(str(bs_obj)) 
    bt.close()
