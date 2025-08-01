function myFunction() {
    document.getElementById("result").innerHTML =
    document.getElementById("demo").firstChild.nodeValue;
    document.getElementById("result").innerHTML =
        document.getElementById("demo").ChildNodes[0].nodeValue;
}