1 调用方式
===
python ISC.py [选项]
 
 -o 输出文件名
 
 -s 开始时间，格式：2005-12-1
 
 -e 结束时间，格式：2006-2-1
 
 -h help

在setting.py 文件中配置请求信息。
如果命令行内输入参数，则自动替换掉setting.py内的输入参数，
如果命令行内不输入参数，则自动读取setting.py内的输入数值


For example:
python ISC.py -o test.txt -s2005-2-1 -e2006-2-1