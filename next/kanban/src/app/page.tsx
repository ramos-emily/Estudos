import Image from "next/image";
import SideBar from "./components/SideBar/page";
import TopBar from "./components/TopBar/page";
import Conteudo from "./pages/Home/page";

export default function Home() {
  return (
    <>
      <TopBar/>
      <SideBar/>
      <Conteudo/>
      <div className="min-w-full min-h-screen bg-blue-100">
        <h1>conteudo page</h1>
      </div>
    </>
  );
}
