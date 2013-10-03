// this file is unused, but it seemed usefull so I kept the code

function getThumbnail(original, scale) {
	var canvas = document.createElement("canvas");

	canvas.width = original.width * scale;
	canvas.height = original.height * scale;

	canvas.getContext("2d").drawImage(original, 0, 0, canvas.width, canvas.height);

	return canvas
}

function setThumb(scale){
	var $this = $(this);
	var original = this.src;
	var canvas = getThumbnail(original,scale);
	if(!canvas);
	$this.parent‘().append(canvas);
}

$("document").ready(function(){
	// call the code to set the images
	var images = $(".thumbnail img");
	if(images.length>0)
		images.each(setThumb(.2));
});