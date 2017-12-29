import time

from ISC.URLs import get_url
from ISC.html_parse import parser
from ISC.setting import *


def start(query):
    html=get_url(query)
    if html:
        if not parser(html,filename):
            print('Failed to download dataset.Try to download data after{}minitues'.format(sleeptime))
            time.sleep(sleeptime*60)
            print('Begine to dowload data again')
            start(query)
    else:
        print('Failed to connect website, Please check if website is valid. And we will try to connect website again')
        time.sleep(sleeptime*60)
        start(query)
if __name__=='__main__':
    start(query)
