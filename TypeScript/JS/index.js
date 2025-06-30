function logar(e){
    e.preventDefault()
    const username = document.getElementById("username").value
    const password = document.getElementById("password").value

    const url = "https://dummyjson.com/auth/login";

    fetch(url, {
        method: "POST",
        headers: { "Content-Type": "application/json"},
        body: JSON.stringify({
            username: username,
            password: password,
        }), 
    }).then(res => res.json()).then(res => {
        if (password != "emilyspass"){
            error.innerHTML = "aaaa ta errado";
        }
        else{
            window.location.href = "./home.html"
        }
    });
}