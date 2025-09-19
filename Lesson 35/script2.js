window.onload = function () {
    let milliseconds = 0;

    let appendmilliseconds = document.getElementById("milliseconds");
    let buttonStart = document.getElementById("btn_start");
    let buttonStop = document.getElementById("btn_stop");
    let buttonRestart = document.getElementById("btn_restart");
    let interval;

    function format(value) {
        return value < 10 ? "0" + value : value;
    }

    buttonStart.onclick = function () {
        clearInterval(interval);
        interval = setInterval(startTimer, 10);
    };

    buttonStop.onclick = function () {
        clearInterval(interval);
    };

    buttonRestart.onclick = function () {
        clearInterval(interval);
        milliseconds = 0;
        appendmilliseconds.innerHTML = "00";
    };

    function startTimer() {
        milliseconds++;

        if (milliseconds > 99) {
            milliseconds = 0;
        }

        appendmilliseconds.innerHTML = format(milliseconds);
    }
} 