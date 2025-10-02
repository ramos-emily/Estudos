export default function Home() {
  return (
    <div>
      <form className="bg-black flex flex-col justify-center text-center w-50 h-50 items-center gap-3">
        <h1 className="text-white font-bold text-lg">Login</h1>
        <div className="bg-white">
          <input type="text" placeholder="Username" />
        </div>
        <div className="bg-white">
          <input type="password" placeholder="Senha" />
        </div>
        <button className="bg-white w-20 ">Logar</button>
      </form>
    </div>
  );
}
