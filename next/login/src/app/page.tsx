"use client"; // precisa para usar hooks no App Router

import { useState } from "react";

export default function Home() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");

  async function handleLogin(e: React.FormEvent) {
    e.preventDefault(); // evita refresh da página

    try {
      const res = await fetch("/api/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password }),
      });

      const data = await res.json();

      if (!res.ok) {
        setMessage(data.error || "Erro ao logar");
        return;
      }

      setMessage("Login realizado com sucesso!");
      // aqui você poderia redirecionar, ex: window.location.href = "/dashboard"
    } catch (err) {
      setMessage("Erro de conexão com o servidor");
    }
  }

  return (
    <div>
      <form
        onSubmit={handleLogin}
        className="bg-black flex flex-col justify-center text-center w-50 h-50 items-center gap-3 p-4"
      >
        <h1 className="text-white font-bold text-lg">Login</h1>

        <div className="bg-white">
          <input
            type="text"
            placeholder="Username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
        </div>

        <div className="bg-white">
          <input
            type="password"
            placeholder="Senha"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </div>

        <button type="submit" className="bg-white w-20">
          Logar
        </button>

        {message && <p className="text-white">{message}</p>}
      </form>
    </div>
  );
}
