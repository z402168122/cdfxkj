# coding=utf-8
import requests
a = '''

upload/images/2015/6/2163848271.jpg
2163848271.jpg

icon_doc.gif

icon_pdf.gif
skins/bg/containIco.gif
containIco.gif
upload/images/2015/6/2163848271.jpg
2163848271.jpg

icon_doc.gif
icon_pdf.gif
skins/bg/bg_4.gif
'''
from urllib import unquote
for r in a.split():
    if  '/' not in r:
        continue
    url = "%s/%s" % ( "http://www.pfeng99.com", r )
    print url
    data = requests.get( url )
    path = "static/" + unquote( r )
    print path
    f = open( path.encode( 'gbk' ) , 'wb' )
    f.write( data.content )
    f.close()





