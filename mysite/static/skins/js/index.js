// JavaScript Document
/*2013.4.8 lyw*/
var url = location.href;
if (url.indexOf("index") > -1 && url.indexOf("?") <0) {
/*新闻滚动*/
var c,_=Function;
var hh = 39;

with(o=document.getElementById("div1"))
{ 
innerHTML+=innerHTML; onmouseover=_("c=1"); onmouseout=_("c=0");
}
(F=_("if(#%hh||!c)#++,#%=o.scrollHeight>>1;setTimeout(F,#%hh?10:3000);".replace(/#/g,"o.scrollTop")))();
/*新闻滚动*/
}