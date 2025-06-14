// Function declaration 
function greetStudent() {
    document.writeln("Hello Student <br>")
}

// Call the function
greetStudent();

// Function as Expression
var goodbye = function () {
    document.writeln("Goodbye, Student <br>");
};

goodbye();

// Function Parameters
function greetByName(name) {
    document.writeln(name + " Welcome to the class! <br>");
}
greetByName("Debashmita");

// Multiple parameters
function multiply(x, y) {
    var result = x* y
    document.writeln(result + "<br>");
}

multiply(4, 2);

// return statemnts
function add(a,b) {
   return a + b;
}

var add_result = add(5,6);
document.writeln(add_result + "<br>");

function square() {
    document.writeln(5 * 5);
}