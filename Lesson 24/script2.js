var i; // i is undefined
var text = "";

{
    let i = 0; // assigning a value for i only within the block
    while (i<7) {
        text += "The value inside the block: " + i + "</br>";
        i++
    }
    document.getElementById("result").innerHTML = text;
}

document.writeln("The value of i outside the block is:" +i);