let choice = prompt("Welcome to Area Calculator. \n Please enter your choice. \n1.Perimeter of Rectangle. \n2.Perimeter of Triangle. \n3.Perimeter of Circle. \n4.Perimeter of Parallelogram"); 

if (choice == "1") {
    const l = prompt("Enter the lenght")
    const w = prompt("Enter the Width")
    const result = 2 * Number(l) + Number(w)
    alert("The perimeter is " + result)
}

else if (choice == "2") {
    const a = prompt("Enter the side")
    const b = prompt("Enter the base")
    const c = prompt("Enter the side")
    const result = Number(a) + Number(b) + Number(c)
    alert("The perimeter  is " + result)
}

else if (choice == "3") {
    const r = prompt("Enter the radius")
    const result =  2 * 3.14 * Number(r) 
    alert("The perimeter  is " + result)
}

else if (choice == "4") {
    const b = prompt("Enter the base")
    const a = prompt("Enter the side")
    const result = 2 * Number(a) + Number(b)
    alert("The perimeter  is " + result)
}