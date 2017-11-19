#coding:utf-8
 
import urllib2,urllib
 
def eazy_url_demo(url):
    res=urllib2.urlopen(url)
    print '>>>>>>>Res info>>'
    print res.info()
    print 'read>>>>>>'
    print res.read()
 
def url_get(url):
    data=urllib.urlencode({'param1':'hello','param2':'wrold'})
    print type(url)
    print type(data)
    new_url='?'.join([url,'%s']) % data
    res=urllib2.urlopen(new_url)
    print '>>>>>>>Res info>>'
    print res.info()
    print 'read>>>>>>'
    print res.read()
 
if __name__=='__main__':
    # url_exp='https://httpbin.org/ip'
    # eazy_url_demo(url_exp)
    url_get1='https://httpbin.org/get'
    url_get1='https://www.baidu.com/'
    
    url_get(url_get1)
    
    