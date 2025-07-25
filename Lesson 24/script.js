var a = 12;
var b = 10;
var c = 10;
var d = "JavaScript";
var e = null;
var f;

document.writeln((a == b) + "<br>");
document.writeln((b == c) + "<br>");
document.writeln(d + "<br>");
document.writeln(e + "<br>");
document.writeln(f + "<br>");

document.writeln("<br>");
var hour = new Date().getHours();
var greet;

if (hour < 12) {
    greet = "Good morning";
}
else if (hour < 18) {
    greet = "Good afternoon";
} else {
    greet = "Good evening";
}

document.writeln("Curent hour: " + hour + "<br>");
document.writeln("Greeting: " + greet + "<br>");

document.writeln("<br>");
let i =1;

while (i <= 10) {
    document.writeln(i + "<br>");
    i = i + 1;
}