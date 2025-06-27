// Array
var skills = ['Scratch', 'MIT APP Inventor' , 'HTML' , 'CSS' , 'BootStrap' , 'JavaScript' ];

// Access values
document.writeln(skills[0] + "<br>")
document.writeln(skills[1] + "<br>")
document.writeln(skills[2] + "<br>")
document.writeln(skills[3] + "<br>")
document.writeln(skills[4] + "<br>")
document.writeln(skills[5] + "<br>")

document.writeln("<br>");
// Arrays methods
// join methods: Convert array into string
document.writeln(skills.join(" - ") + "<br><br>");

// pop method: remove the last element from the array
skills.pop();
skills.pop();
skills.pop();
document.writeln(skills + "<br><br>");

// Call Stack: Track the funcion calling

function func1() {
    document.writeln("func1() started.<br>")
    func2();
    document.writeln("func1() ended.<br>");
}

function func2() {
    document.writeln("func2() started.<br>")
    func3();
    document.writeln("func2() ended.<br>");
}

function func3() {
    document.writeln("func3() started.<br>")
    document.writeln("func3() ended.<br>");
}

func1();