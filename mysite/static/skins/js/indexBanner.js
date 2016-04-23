/*index_ban*/
var tt=0;
var stime2=5000;
var objM=$(".banUL ul li");
var sss=objM.length;

$(function(){	
	$(".Inbanner").append("<div class='control'><p></p></div>");
	
	for(z=0;z<objM.length;z++){
		$(".control p").append("<span>&nbsp;</span>");
		var src=objM.eq(z).find("img").attr("src");
		objM.eq(z).find("a").css("background","url("+src+") no-repeat center top");
	}
	$(".control span").eq(0).addClass("ibC");	
	objM.eq(0).fadeIn(800);
	
	$(".control span").hover(function(){
		clearInterval(Auto2);
		var ibnum=$(".control span").index(this);		
		$(".control span").removeClass("ibC");
		$(".control span").eq(ibnum).addClass("ibC");		
		objM.fadeOut(200);		
		objM.eq(ibnum).fadeIn(800);
		tt=ibnum;

	},function(){Auto2=setInterval(iBan,stime2);	});

});

function iBan(){
		tt++;
		if(tt < sss){
			$(".control span").removeClass("ibC");
			$(".control span").eq((tt)).addClass("ibC");		
			objM.fadeOut(200);		
			objM.eq((tt)).fadeIn(800);
		}else if(tt == sss){
			tt=0;
			$(".control span").removeClass("ibC");
			$(".control span").eq((tt)).addClass("ibC");		
			objM.fadeOut(200);		
			objM.eq((tt)).fadeIn(800);			
		}
}

var Auto2=setInterval(iBan,stime2);		

/*index_ban*/