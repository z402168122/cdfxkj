# coding=utf-8
import requests
a = '''
upload/images/2015/6/2163824996.jpg
upload/images/2015/1/%E4%BA%A7%E5%93%81%E5%88%97%E8%A1%A8%E9%A1%B5-R25.jpg
upload/images/2015/1/%E4%BA%A7%E5%93%81%E5%88%97%E8%A1%A8%E9%A1%B5-%E5%85%A5%E5%A2%99%E5%BC%8FAP.jpg
upload/images/2015/1/%E4%BA%A7%E5%93%81%E5%88%97%E8%A1%A8%E9%A1%B5-%E7%BD%91%E7%BA%BF.jpg
upload/images/2015/1/%E6%9C%8D%E5%8A%A1%E5%99%A8%E5%B0%8F.jpg
upload/images/2015/3/%E7%BD%91%E5%90%A7.jpg
skins/js/swfobject.js
skins/js/jwplayer.js
skins/js/jquery-1.7.min.js
skins/js/common.js
skins/js/index.js
skins/js/indexBanner.js
indexBanner.js
upload/images/2015/3/%E9%85%92%E5%BA%97.jpg
酒店.jpg
upload/images/2015/3/%E6%A1%88%E4%BE%8B.jpg
案例.jpg
upload/images/2015/5/2132512679.png
2132512679.png
upload/images/2015/5/22181154187.jpg
22181154187.jpg
upload/images/2015/5/216555779.jpg
216555779.jpg
upload/images/2015/5/22181514986.jpg
22181514986.jpg
upload/images/2015/5/213312314.jpg
213312314.jpg
upload/images/2015/6/2163824996.jpg
2163824996.jpg
upload/images/2015/1/%E4%BA%A7%E5%93%81%E5%88%97%E8%A1%A8%E9%A1%B5-R25.jpg
产品列表页-R25.jpg
upload/images/2015/1/%E4%BA%A7%E5%93%81%E5%88%97%E8%A1%A8%E9%A1%B5-%E5%85%A5%E5%A2%99%E5%BC%8FAP.jpg
产品列表页-入墙式AP.jpg
upload/images/2015/1/%E4%BA%A7%E5%93%81%E5%88%97%E8%A1%A8%E9%A1%B5-%E7%BD%91%E7%BA%BF.jpg
产品列表页-网线.jpg
upload/images/2015/1/%E6%9C%8D%E5%8A%A1%E5%99%A8%E5%B0%8F.jpg
服务器小.jpg
upload/images/2015/3/%E7%BD%91%E5%90%A7.jpg
网吧.jpg
skins/js/swfobject.js
swfobject.js
upload/images/2015/3/%E9%85%92%E5%BA%97.jpg
酒店.jpg
upload/images/2015/3/%E6%A1%88%E4%BE%8B.jpg
案例.jpg
upload/images/2015/5/2132512679.png
2132512679.png
skins/js/jwplayer.js
jwplayer.js
skins/js/jquery-1.7.min.js
jquery-1.7.min.js
upload/images/2015/5/22181154187.jpg
22181154187.jpg
upload/images/2015/5/216555779.jpg
216555779.jpg
upload/images/2015/5/22181514986.jpg
22181514986.jpg
upload/images/2015/5/213312314.jpg
213312314.jpg
skins/js/jquery-1.7.min.js
jquery-1.7.min.js
skins/js/common.js
common.js
skins/js/index.js
index.js
skins/js/indexBanner.js
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





