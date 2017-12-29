import re
def parser(html,filename):

    f=open('result.html','w')
    f.write(html)
    fw=open(filename,'w')
    pattern='LON.*?(<a .*?)STOP'
    items=re.findall(pattern,html,re.S).pop().strip().split('\n')
    if items:
        for item in items:
            item_tem=item.strip().split(',')
            for item_fin in item_tem:
                if '<a' in item_fin:
                    item_out=re.findall('<a.*>(.*?)</a>',item_fin,re.S).pop()
                else:
                    item_out=item_fin.strip()
                if item_out=='':
                    item_out='None'
                fw.write(item_out.ljust(15))
            fw.write('\n')
        return True
    else:
        print('Failed to Download data ')
        return None