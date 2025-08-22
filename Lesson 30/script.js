let choice = prompt("Welcome to Area Calculator. \n Please enter your choice. \n1.Area of Rectangle. \n2.Area of Triangle. \n3.Area of Circle. \n4.Area of Parallelogram");

if (choice == "1") {
    const l = prompt("Enter the lenght")
    const b = prompt("Enter the breadth")
    const result = Number(l) * Number(b)
    alert("The area is " + result)
}

 else if (choice == "2") {
    const h = prompt("Enter the height")
    const b = prompt("Enter the base")
    const result = Number(h) * Number(b) /2
    alert("The area is " + result)
}

else if (choice == "3") {
    const r = prompt("Enter the radius")
    const result = 3.14 * Number(r) * Number(r) 
    alert("The area is " + result)
}

else if (choice == "4") {
    const h = prompt("Enter the height")
    const cb = prompt("Enter the corresponding base")
    const result = Number(h) * Number(cb)
    alert("The area is " + result)
}
