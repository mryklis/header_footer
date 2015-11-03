import sys
import os
from datetime import date, datetime

##define header
header= str(('O*NXXX         73          O*N0XTG7XXX      ,CLS=CRDLXXX,XXX,BAT=,'))
##define trailer
trailer=str(('O*N95TXXXX         ,CLS=CRDLXXX,XXX,BAT=,        O*NXX            73'))

##process all files in directory
for file in os.listdir('PATH'):
    file_name=file
    path = os.path.normpath('PATH')
    ##create new file name with date appended to end
    file_date=date.today().strftime("%y%m%d")
    new_file_name=file_name+file_date
    ##create new file with new name
    new_file=open(new_file_name, 'a')
    ##append header
    with new_file as f:
        f.write(header)
        f.write("\n")
        f.close
    ##read contents of original file and write line by line to new file    
    test_file=open(path+"/"+file_name, 'r')
    for line in test_file:
        new_file=open(new_file_name, 'a')
        with new_file as f:
            f.write(line)
    ##append footer to file
    new_file=open(new_file_name, 'a')
    with new_file as f:
        f.write(trailer)
        f.close
