import sys
import getopt
from schedule import start
from setting import *
def get_args():
    try:
        opts,args=getopt.getopt(sys.argv[1:],'ho:s:e:')
    except getopt.GetoptError as err:
        print(err)
        sys.exit(2)
    status=True
    if opts:
        for opt,arg in opts:
            if '-o' in opt:
                global filename
                filename=arg
            elif '-s' in opt:
                Sy=arg.split('-')[0]
                Sm=arg.split('-')[1]
                Sd=arg.split('-')[2]
            elif '-e' in opt:
                Ey=arg.split('-')[0]
                Em=arg.split('-')[1]
                Ed=arg.split('-')[2]
            elif '-h' in opt:
                status=False
                print('-s'.ljust(10),'start_time: end_year-end_month-end_day')
                print('-e'.ljust(10),'end_time: end_year-end_month-end_day')
                print('-o'.ljust(10),'filename:outfilename.txt')
                print('For example:python ISC -s2005-1-1 -e2016-1-1,-o filename.txt')
        keys=['start_year','start_month','start_day','end_year', 'end_month','end_day']
        try:
            for key,value in zip(keys,[Sy,Sm,Sd,Ey,Em,Ed]):
                query[key]=value
        except:
            pass
    if status:
        start(query,filename)
if __name__=='__main__':
    get_args()
