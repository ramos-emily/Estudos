import { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router';

function Login() {
  const [username, setUsername] = useState<string>();
  const [password, setPassword] = useState<string>(); 
  const [error, setError] = useState<string>();
  const navigator = useNavigate();

  const onLogin = async () => {
    try {
      const request = await axios.post('https://dummyjson.com/auth/login', {
        username: username,
        password: password,
      });
      if (request.status === 200) {
        navigator("/home");
      }
    } catch {
      setError("Erro ao fazer login. Verifique suas credenciais.");
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center ">
      <div className="bg-white p-8 rounded-lg shadow-sm border border-gray-200 w-full max-w-xs">
        <h2 className="text-2xl font-semibold mb-6 text-center text-gray-800">Login</h2>
        
        <div className="mb-4">
          <input 
            type="text" 
            placeholder="Usuário"
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:border-blue-500" 
            onChange={(e) => setUsername(e.target.value)}
          />
        </div>

        <div className="mb-6">
          <input 
            type="password" 
            placeholder="Senha"
            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:border-blue-500" 
            onChange={(e) => setPassword(e.target.value)}
          />
        </div>

        {error && <p className="text-red-500 text-xs mb-4 text-center">{error}</p>}

        <button 
          onClick={onLogin} 
          className="w-full bg-blue-500 hover:bg-blue-600 text-white py-2 px-4 rounded-md transition-colors"
        >
          Entrar
        </button>
      </div>
    </div>
  );
}

export default Login;