const button = document.getElementById("btn");
button.addEventListener("click",()=>{
    const title = document.getElementById("title").value;
    const body = document.getElementById("body").value;
    fetch("https://jsonplaceholder.typicode.com/posts", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            title: title,
            body: body,
            userId: 1
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("result").innerHTML = `<h3>Data Sent Successfully</h3>
        <p><b>Title : </b> $ {data.body}</p>`;
        console.log(data);
    })
    .catch(error => {
        console.log(error);
    });
});
