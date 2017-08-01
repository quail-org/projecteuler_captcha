chrome.extension.sendMessage({}, function(response) {
	var readyStateCheckInterval = setInterval(function() {
	if (document.readyState === "complete") {
		clearInterval(readyStateCheckInterval);

		// ----------------------------------------------------------
		// This part of the script triggers when page is done loading
		console.log("Hello. This message was sent from scripts/inject.js");
		// ----------------------------------------------------------
        
        //https://stackoverflow.com/questions/934012/get-image-data-in-javascript
        var captcha = document.getElementById("captcha_image");

        var canvas = document.createElement("canvas");
        canvas.width = captcha.width;
        canvas.height = captcha.height;

        var ctx = canvas.getContext("2d");
        ctx.drawImage(captcha, 0, 0);
        
        var dataURL = canvas.toDataURL("image/png");
        console.log(dataURL.replace(/^data:image\/(png|jpg);base64,/, ""));
    }
	}, 10);
});
