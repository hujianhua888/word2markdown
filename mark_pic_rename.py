# -*- coding: utf-8 -*-
import re
from re import sub  
import sys
import os

 
save_file='./output.txt'

def main():
    inpath = '.\语音.md'
    uipath = unicode(inpath , "utf8") 
    md_file=open(uipath,'r')
    file_list  = []
    num = 0
    for line in md_file:
        text = line.strip()
        match_flag = re.match( r'(.*media\/.*\.png)', text)
        match_flag_jpg = re.match( r'(.*media\/.*\.jpg)', text)
        if match_flag:           
            #print('-----------'+str(text))
            one_file_list = re.findall(r'(media\/.*\.png)',text)
            #print(one_file_list[0])
            one_file_list.append('png')
            file_list.append(one_file_list)
            #get_char = re.search( r'(media\/.*\.png)', line)
            #if get_char:
            #    print(get_char)
        elif match_flag_jpg:
            one_file_list = re.findall(r'(media\/.*\.jpg)',text)
            one_file_list.append('jpg')
            file_list.append(one_file_list)           
            
    for f_elment in file_list:
        #print(f_elment)
        f = f_elment[0]
        t = f_elment[1]
        
        print(str(num) +'=>'+ f) 
        cmdline = 'mv ./'+f+' ./media/'+str(num)+'.'+t
        print cmdline
        os.system(cmdline)
        num = num + 1
        #break

    md_file.close()

    





    
  
  
if __name__ == '__main__':  
    main()
