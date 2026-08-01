const toastElement =document.getElementById("myToast");
const toast  = new bootstrap.Toast(toastElement);

document.getElementById("btn").addEventListener("click", ()=>{
    toast.show();
});