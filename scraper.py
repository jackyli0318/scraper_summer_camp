#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 11:03:48 2017

@author: jackylee
"""
from bs4 import BeautifulSoup
import re
import time
import urllib.request
import codecs


def run_search(url, keyword):
    html=None
    
    fw=open('links.txt','w+') 
    with fw:
        
        for i in range(5):
            try:
                
                req = urllib.request.Request(url, headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',})
                oper = urllib.request.urlopen(req)
                html = oper.read()
    #                html = str(oper.read(),'utf-8')
    #                response=requests.get(pageLink,headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', })
    #                html=response.content 
    #                str(response.read(),'utf-8')
                break 
            except Exception as e:
                print ('failed attempt',i)
                time.sleep(0.1) 
    				
            if not html:
                continue 
        
        soup = BeautifulSoup(html.decode('utf-8'),'lxml') 
    
        tags=soup.findAll('a', {'title':re.compile('查看详情')})
        print("reading data...\n")
        for tag in tags:
    #        source = tag.find('a',{'href':''})
            link = tag.get('href')
            print(link)
            fw.write("https://www.xialingying.cc" + str(link)+ "\n")
            
        time.sleep(1)
        fw.close()

    

def single_web():
    linklst = list()
    
    f=open('links.txt','r')
    
    with f:
        linelst = f.readlines()
        for line in linelst:
            linklst.append(line.strip())
            
        f.close()
    
    fw=codecs.open('outputs.txt','w+', encoding='utf-8') 
    
    with fw:
        for url in linklst:

            html=None
    		
            for i in range(5):
                try:
                    
                    req = urllib.request.Request(url, headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',})
                    oper = urllib.request.urlopen(req)
                    html = oper.read()
                    break 
                except Exception as e:
                    print ('failed attempt',i)
                    time.sleep(0.1) 
    				
    		
                if not html:
                    continue 
            
            soup = BeautifulSoup(html.decode('utf-8'),'lxml') 
    
            tags=soup.findAll('div', {'class':re.compile('tak_con_bot')})
            print("reading data...\n")
            
            for tag in tags:
    
                text = str(tag.text.strip())
                
#                print(url+"\n")
                print(text+"\n")
                fw.write(url+"\n" + text+"\n")
                
                time.sleep(0.1)	
            time.sleep(1)

    fw.close()
    


if __name__=='__main__':

#    url = 'https://www.xialingying.cc/america/'
#    run_search(url, '')
    
#    url = 'https://www.xialingying.cc/xindongfang/course/1479180049.html'
    single_web()

    
    







