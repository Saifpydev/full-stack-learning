console.log("Bootstrap Buttons Loaded");
let buttons = document.querySelectorAll(".btn");
buttons.forEach(function(button){
    button.addEventListener("click",function(){
        console.log(button.innerText);
    });
});