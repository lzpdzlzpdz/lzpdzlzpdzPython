#coding:utf-8
 
import requests
 
def eazy_url_demo(url):
    res=requests.get(url)
    print '>>>>>>>Res info>>'
    print res.headers
    print 'read>>>>>>'
    print res.text
 
def url_get(url):
    data={'param1':'hello','param2':'wrold'}
    res=requests.get(url,params=data)
    print '>>>>>>>code'
    print res.status_code
    print res.reason
    print '>>>>>>>Res info>>'
    print res.headers
    print 'read>>>>>>'
    print res.text
 
if __name__=='__main__':
    # url_exp='https://httpbin.org/ip'
    # eazy_url_demo(url_exp)
    url_get1='https://httpbin.org/get'
    url_get(url_get1)
    
    