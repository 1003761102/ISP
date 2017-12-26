
# Download Arrivals from [ISC](http://www.isc.ac.uk/iscbulletin/search/arrivals/) #

This is a collection of scripts for ISC catalogue data request and download.

## Dependency ##
- python 3.4
- Python modules
  - `request`
  - `re`
  - `get` `query` `public` `post`

For Mac OSX

      sudo python3 -m pip install requests
      sudo python3 -m pip install get query-string public post
  
## Usage ##

1. 在`setting.py`文件中配置请求信息。

2. filename为输出文件名，query为请求台站的参数信息。

3. 运行`schedule.py`即可。
