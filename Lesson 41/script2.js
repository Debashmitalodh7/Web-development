var index = 0;
carousel();

function carousel() {
    var i;
    var x = document.getElementsByClassName("myslides");
    for (i = 0; i < x.length; i++) {
        x[i].style.display = "none";
    }
    index++;
    if (myIndex > x.length) {myIndex = 1}
    x[index - 1].style.display = "block";
    setTimeout(carousel, 3000);
}
carousel(); // Start the carousel when the page loads