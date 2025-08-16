function validationForm(event) {
    event.preventDefault();

    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    let message;


    if (email == "") {
        message = "Email is requried";
        document.getElementById("validation_message").style.color = "red";
    }

    else if (password == "")  {
        message = "password is required";
        document.getElementById("validation_message").style.color = "red";
    }

    else {
        message= "Form submitted!";
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