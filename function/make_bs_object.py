import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

def makeBSOjc(url):
    html = urlopen(url)  
    bsObject = BeautifulSoup(html, "html.parser")
    return bsObject