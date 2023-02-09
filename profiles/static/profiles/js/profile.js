const saveProfileBtn = document.getElementById("saveProfileBtn");
saveProfileBtn.style.display = "none";
const saveCardBtn = document.getElementById("saveCardBtn");
saveCardBtn.style.display = "none";

function enableProfileForm() {
let saveProfileBtn = document.getElementById("saveProfileBtn");
saveProfileBtn.style.display = "flex";
var form = document.getElementById("profileForm");
var inputs = form.getElementsByTagName("input");
for (var i = 0; i < inputs.length; i++) {
 inputs[i].disabled = false;
let editProfileBtn = document.getElementById("editProfileBtn");
editProfileBtn.style.display = "none";
}
}
function disableProfileForm() {
var form = document.getElementById("profileForm");
var inputs = form.getElementsByTagName("input");
for (var i = 0; i < inputs.length; i++) {
 inputs[i].disabled = true;
}
let saveProfileBtn = document.getElementById("saveProfileBtn");
saveProfileBtn.style.display = "none";
}
function enableCardForm() {
var form = document.getElementById("CardForm");
var inputs = form.getElementsByTagName("input");
for (var i = 0; i < inputs.length; i++) {
 inputs[i].disabled = false;
}
let saveCardBtn = document.getElementById("saveCardBtn");
saveCardBtn.style.display = "flex";
let editCardBtn = document.getElementById("editCardBtn");
editCardBtn.style.display = "none";
}
function disableCardForm() {
var form = document.getElementById("CardForm");
var inputs = form.getElementsByTagName("input");
for (var i = 0; i < inputs.length; i++) {
 inputs[i].disabled = false;
}
let saveCardBtn = document.getElementById("saveCardBtn");
saveCardBtn.style.display = "none";
}
function validateLength(input) {
if (input.value.length < 3) {
 input.value = input.value.slice(0, 3);
}
if (input.value.length > 3) {
 input.value = input.value.slice(0, 3);
}
}
