// Array
var student = [ 'karina' , '15' , '9' ,  'Drawing'];

// Access values
document.writeln(student[0] + "<br>")
document.writeln(student[1] + "<br>")
document.writeln(student[2] + "<br>")
document.writeln(student[3] + "<br>")

document.writeln("<br>");
// Arrays methods
// join methods: Convert array into string
document.writeln(student.join(" - ") + "<br><br>");

// pop method: remove the last element from the array
student.pop();
student.pop();
student.pop();
document.writeln(student + "<br><br>");

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

func1()