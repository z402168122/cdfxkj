// JavaScript Document
/*2013.4.8 lyw*/

$(function(){
	/*头部 地区链接下拉*/	
	$(".area").hover(function(){
		$(this).find("p").slideDown(200);	
		},function(){
		$(this).find("p").hide();	
	});
	
	
	
	/*头部导航 下拉菜单*/
	$(".nav li").hover(function(){
		$(this).find("a:first").addClass("cur");	
		$(this).find(".Drop").slideDown(200);
		},function(){
		$(this).find("a:first").removeClass("cur");	
		$(this).find(".Drop").hide(0);	
	});
	
	var tsrc=$(".Isbanner").find("img").hide().attr("src");
	$(".Isbanner").css("background","url("+tsrc+") no-repeat center top");
	
	/*接口人员信息列表*/
	if($(".renIF").length>0){
		for(var i=0;i<$(".renIF tr").length;i++){
			if(i%2 == 0){
				$(".renIF tr").eq(i).addClass("hsbg");	
			}	
		}
	};
	
	/*行业解决方案*/
	if($(".IndList").length>0){
		for(var i=0;i<$(".IndList li").length;i++){
			if(i%2 != 0){
				$(".IndList li").eq(i).addClass("lihg");	
			}	
		}
	};
	
	/*行业解决方案 详细页图片背景*/
	if($(".CaseBox").length>0){
		for(var i=0;i<$(".CaseBox img").length;i++){
			$(".CaseBox img").eq(i).addClass("ImgTY");	
			
		}
	};
	
	/*行业支持 tab切换*/
	if($(".SupportTabTop").length>0){
		$('.SupportTabTop span').eq(0).addClass("spcur");
		$('.SupportTabCon .SPBox').eq(0).addClass('bk');
		
		$('.SupportTabTop span').click(function(){
		var vi=	$('.SupportTabTop span').index(this);
		$(this).addClass('spcur').siblings().removeClass('spcur');
		$('.SupportTabCon .SPBox').removeClass('bk');
		$('.SupportTabCon .SPBox').eq(vi).addClass('bk');
		});	
	}
	
	/*proList*/
	if($(".proList").length>0){
		$(".proList li").hover(function(){
			$(this).css("background-position","0 -149px")	
			},function(){
			$(this).css("background-position","0 0px")		
		});
	}
	
	/*产品参数 表格背景*/
	if($(".proTable").length>0){
		for(var i=0;i<$(".proTable tr").length;i++){
			if(i%2 != 0){
				$(".proTable tr").eq(i).addClass("hsbg");	
			}	
		}
	}
	
	
	/*产品详细页 tab切换*/
	if($(".proTab").length>0){
//		$('.PTDTop span').eq(0).addClass("ptspcur");
//		$('.PTDCon .PTDBox').eq(0).addClass('bk');
		
		$('.PTDTop span').click(function(){
		var vi=	$('.PTDTop span').index(this);
		$(this).addClass('ptspcur').siblings().removeClass('ptspcur');
		$('.PTDCon .PTDBox').removeClass('bk');
		$('.PTDCon .PTDBox').eq(vi).addClass('bk');
		});	
	}
	
	/*多媒体 主页 月刊tab*/
	$(".ykSel span").click(function(){
		var vi=	$('.ykSel span').index(this);
		$(".year em").html($('.ykSel span').eq(vi).html());
		$(this).addClass('ykcur').siblings().removeClass('ykcur');
		$('.jourSel p').removeClass('bk');
		$('.jourSel p').eq(vi).addClass('bk');	
	});
	
	
	/*公司期刊*/
	if($(".jourList").length>0){
		for(var i=0;i<$(".jourList li").length;i++){
			if(i%2 != 0){
				$(".jourList li").eq(i).addClass("lihg");	
			}	
		}
	};
	
	
	
	
})

	/* 招聘信息上拉菜单 */
function show() {
		$(".adv_word").slideToggle();
	};