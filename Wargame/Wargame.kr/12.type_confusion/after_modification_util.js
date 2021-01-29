function submit(key){
	$.ajax({
		type : "POST",
		async : false,
		url : "./index.php",//       %%%%%%%%%
		data : {json:JSON.stringify({key: true})},
		dataType : 'json'//          %%%%%%%%%
	}).done(function(result){
		if (result['code'] == true) {
			document.write("Congratulations! flag is " + result['flag']);
		} else {
			alert("nope...");
		}
		lock = false;
	});
}
