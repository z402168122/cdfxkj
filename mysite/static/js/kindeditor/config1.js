KindEditor.ready(function(K) {
    
    K.create('#id_detail'+i,{
	        // 指定大小
	        width:'800px',
	        height:'500px',
	        allowPreviewEmoticons : true,
			allowImageUpload : true,
			uploadJson : '/update_img',
			items : [
				'fontname', 'fontsize', '|', 'forecolor', 'hilitecolor', 'bold', 'italic', 'underline',
				'removeformat', '|', 'justifyleft', 'justifycenter', 'justifyright', 'insertorderedlist',
				'insertunorderedlist', '|', 'emoticons', 'image', 'link']
	    });     
});

