function showCalander() {
    let date = new Date();
    let d= date.getDate();
    let m = date.getMonth();
    let y = date.getYear();


var calander = "Date: " + date +"/"+ month +"/"+ year + "Day: " + today;
document.getElementById("Mycalander").innerText = calander; 

}

showCalander();