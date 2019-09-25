socket = new WebSocket("ws://localhost:8000/apollo/");
socket.onmessage = function(e) {
        //alert("Hello!!!!");
	//alert(e.data);
	
	//Special char \\ were observed in the text
	//Also " was present at start and end of the string
	var strdata=e.data.replace(/\\/g,'');
	strdata=strdata.substring(1,strdata.length-1);
	//alert("strdata="+strdata);
	var obj=JSON.parse(strdata);
	var properties="";
	//iterate over the JSON object and create a single string to display
	for(var i in obj){
		properties += (i+">>"+obj[i]+"<br>");
	}
	
	document.getElementById("displayNode").innerHTML = properties;

}
socket.onopen = function() {
    //alert("WebSocket connection is open now");
    socket.send("socket opened");
}

if (socket.readyState == WebSocket.OPEN) socket.onopen();
