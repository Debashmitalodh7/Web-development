let form = document.getElementById("shoppingform");
let input = document.getElementById("shoppinginput");
let items = document.getElementById("items");

form.addEventListener("submit", function (event) {
    event.preventDefault();
    createItem(input.value);
});

function createItem(inputitem) {
    let item = `<li>${inputitem} <button onclick="deleteItem(this)">Delete</button></li>`;
    items.insertAdjacentHTML("beforeend", item);
    input.value = "";
    input.focus();
}

function deleteItem(element) {
    element.parentElement.remove();
}