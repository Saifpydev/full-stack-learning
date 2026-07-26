const btn = document.getElementById("btn");
const result = document.getElementById("result");
btn.addEventListener("click", () => {
    fetch("https://jsonplaceholder.typicode.com/posts/1")
    .then(response =>{ 
        if(!response.ok){
            throw new Error("API Error : " + response.status);
        }
        return response.json();
    })
    .then(data =>{
        result.innerHTML = `<h3>Data Loaded Successfully </h3>
        <p><b>ID : </b> $ {datatitle}>/p>`;
    })
    .catch(error => {
        result.innerHTML = `<h3>style="color:red;">Error </h3>
        <p>${error.message}</p>`;
        console.log(error);
    });
});
