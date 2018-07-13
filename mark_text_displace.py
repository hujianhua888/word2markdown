# -*- coding: utf-8 -*-
import re
from re import sub  
import sys
import codecs
import os
#import chardet

reload(sys)
sys.setdefaultencoding('utf8') #因为中文乱码问题，加上此代码
print sys.getdefaultencoding() + "  - sys.getdefaultencoding()"


def main():
    inpath = '.\\语音.md'
    input_f_name = '.\\f.txt'
    output_md_name = '.\\output.md'
    input_f_name = unicode(input_f_name , "utf8") 
    uipath = unicode(inpath , "utf8") 
    md_file=open(uipath,'r')
    file_list  = []
    num = 0

    #f=open(input_f_name,'rb')
    #f_read=f.read()
    #f_charInfo=chardet.detect(f_read)
    #print(f_charInfo['encoding'])
    #f_charInfo的输出是这样的的一个字典{'confidence': 0.99, 'encoding': 'utf-8'}
    #f.close()  
        
    name_file=open(input_f_name,'rb') 
       
    #f_read=name_file.read()
    #f_read_decode=f_read.decode('gbk')
    
    out_file=open(output_md_name,'w')
    #out_file = codecs.open(output_md_name,'w+','utf-8')
    name_list  = []
    
    #sys.exit()
  
    for d_str in name_file:
        f_read_decode = d_str.decode('gbk')
        d_str = f_read_decode
        #print(str(num) +'=>'+ d_str)
        name_list.append(d_str)
        num = num + 1

    num = 0
 

    #print '准备写入文件：{}'.format(output_md_name)    
    for line in md_file:
        #print(type(line))
        text = line.strip()
        match_flag = re.match( r'(.*media\/.*\.png)', text)
        match_flag_jpg = re.match( r'(.*media\/.*\.jpg)', text)
        if match_flag or match_flag_jpg:
            print(str(num) +'=>'+ name_list[num])
            out_file.write(name_list[num])
            out_file.write('\n')
            #out_file.write('\n')
            num = num + 1
        else:
            out_file.write(line)
        

    md_file.close()
    out_file.close

    





    
  
  
if __name__ == '__main__':  
    main()
