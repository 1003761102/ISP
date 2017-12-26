from URLs import get_url
from setting import *

from html_parse import parser

if __name__=='__main__':
    html=get_url(query)
    if html:
        parser(html,filename)