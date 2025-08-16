// String Methods
var text = "I am Debashmita";
document.writeln(text.toUpperCase() + "<br>");
document.writeln(text.toLowerCase() + "<br>");
document.writeln(text.startsWith("Debashmita") + "<br>");

// Regular Expression 
var regexp = new RegExp("Debashmita");
var result = regexp.test(text);
document.writeln(result + "<br>");

// Loops : For Loop
for (var i = 1; i <= 50; i = i + 1) {
    document.writeln(i);
}

document.writeln("<br>");
// Swiitch-Case
var today = new Date().getDay();
var display_day;

switch (today) {
    case 0:
        display_day = "Sunday";
        break;
    case 1:
        display_day = "Monday";
        break;
    case 2:
        display_day = "Tuesday";
        break;
    case 3:
        display_day = "Wednesday";
        break;
    case 4:
        display_day = "Thursday";
        break;
    case 5:
        display_day = "Friday";
        break;
    case 6:
        display_day = "Saturday";
        break;
    default:
        display_day = "Invalid day";
}

document.writeln(display_day);