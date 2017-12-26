import requests
def get_url(query):
    headers={
        'Referer':'http://isc-mirror.iris.washington.edu/iscbulletin/search/arrivals/',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'
    }
    try:
        base_url = 'http://isc-mirror.iris.washington.edu/cgi-bin/web-db-v4'
        r=requests.get(base_url,params=query,headers=headers)
        return r.text
    except:
        print('Failed to download html')
