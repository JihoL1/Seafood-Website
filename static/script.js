var index = 0;
slides();
/* function for automatic slideshow */
function slides() {
    var i;
    var x = document.getElementsByClassName("slide");
    for (i =0; i < x.length; i++) {
        x[i].style.display = "none";
    }
    index++;
    if (index > x.length) {index = 1};
    x[index-1].style.display = "block";
    /* change slide every 4 seconds */
    setTimeout(slides, 4000);
}