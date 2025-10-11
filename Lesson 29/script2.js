function validationForm(event) {
    event.preventDefault();

    const name = document.getElementById("name").value;
    const password = document.getElementById("age").value;
    let message;


    if (Name == "") {
        message = "Name is requried!!";
        document.getElementById("validation_message").style.color = "red";
    }

    else if (age== "") {
        message = "Age is required!!";
        document.getElementById("validation_message").style.color = "red";
    }


    else {
        message = "Form submitted!";
        document.getElementById("validation_message").style.color = "green";
    }
    document.getElementById("validation_message").innerText = message;
}

function validateNumber() {
    const numElement = document.getElementById("number");
    let message;
    if (numElement.checkValidity() == false) {
        message = numElement.validationMessage;
    } else {
        message = "OK";
    }
    document.getElementById("message").innerText = message;
}