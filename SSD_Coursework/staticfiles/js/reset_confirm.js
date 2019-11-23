

var inputs = document.getElementsByTagName("input");

inputs[1].placeholder = ('Enter a new password');

inputs[2].placeholder = ('Confirm your new password');

var errorList = document.getElementsByClassName('errorlist')[0];
errorList.style.listStyleType = "none";
errorList.style.color = "#ff584d";
