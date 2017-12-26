import re
from setting import keys
def parser(html,filename):
    fw=open(filename,'w')
    pattern='LON.*?(<a .*?)STOP'
    items=re.findall(pattern,html,re.S).pop().strip().split('\n')
    for item in items:
        item_tem=item.strip().split(',')
        for item_fin,key in zip(item_tem,keys):
            if '<a' in item_fin:
                item_out=re.findall('<a.*>(.*?)</a>',item_fin,re.S).pop()
            else:
                item_out=item_fin.strip()
            fw.write(item_out+'\t')
        fw.write('\n')