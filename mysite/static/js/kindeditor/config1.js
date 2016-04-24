KindEditor.ready(function(K) {
    window.editor = K.create('#id_detail',{

        // 指定大小
        width:'800px',
        height:'500px',
        allowPreviewEmoticons : false,
		allowImageUpload : false,
		items : [
			'fontname', 'fontsize', '|', 'forecolor', 'hilitecolor', 'bold', 'italic', 'underline',
			'removeformat', '|', 'justifyleft', 'justifycenter', 'justifyright', 'insertorderedlist',
			'insertunorderedlist', '|', 'emoticons']
    });
});

