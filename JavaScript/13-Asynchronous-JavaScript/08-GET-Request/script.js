const  btn = document.getElementById("btn");
const result = document.getElementById("result");
btn.addEventListener("click", function (){
    fetch("https://jsonplaceholder.typicode.com/users/1",{
        method: "GET"
    })
    .then(function(response){
        return response.json();
    })
    .then(function(data){
        result.innerHTML = `<h2>${data.name}</h2>
        <p>Email: ${data.email}></p>
        <p>Phone: ${data.phone}</p>`;
        console.log(data);
    })
    .catch(function(error){
        console.log("Error:",error);
    });
});