var keydown = 0
var Texte = ""
var doc = window.document;

function func_KeyDown(event){
    if (doc.location.href.includes('picture'))
    {
	keydown = (window.Event) ? event.which : event.keyDown;
	switch(keydown) {
	case 37: //left arrow
	    doc.location.href = '/prev'; break
	case 39: //right arrow
	    doc.location.href = '/next' ; break
	case 80: //p
	    doc.location.href = '/keep' ; break
	case 88: //x
	    doc.location.href = '/reject' ; break
	}
	var keydown = 0
	var Texte = ""
    }
}
