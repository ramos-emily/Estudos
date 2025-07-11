function logar(e){
    e.preventDefault()
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    const error = document.getElementById("error");

    const url = "https://dummyjson.com/auth/login";

    fetch(url, {
        method: "POST",
        headers: { "Content-Type": "application/json"},
        body: JSON.stringify({
            username: username,
            password: password,
        }), 
    }).then(res => {
        if (!res.ok) {
            throw new Error("Login inválido");
        }
        return res.json();
    }).then(data => {
        window.location.href = "./home.html"
    }).catch(err => {
        error.innerText = "Usuario ou senha incorretos.";
    });
}