function isPalindrome(event) {
    event.preventDefault();

    let text = document.getElementById("userinput").value;
    const pelement = document.getElementById("result");
    if (text == "") {
        pelement.innerText = "Please write a text"
    } else {
        const originaltext = text;
        lowertext = text.toLowerCase();
        // convert the string into an array
        splitted = lowertext.split("");
        // reverse the array
        reversed = splitted.reverse();
        // convert the reversed array into string
        reversedstring = reversed.join("");

        if (reversedstring == lowertext) {
            pelement.innerText = originaltext + " is a palindrome. ";
        } else {
            pelement.innerText = originaltext + " is not a palindrome. ";
        }
    }
}