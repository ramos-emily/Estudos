import Image from "next/image";
import SideBar from "./components/SideBar/page";
import TopBar from "./components/TopBar/page";

export default function Home() {
  return (
    <>
      <TopBar/>
      <SideBar/>
      <div className="min-w-full min-h-screen bg-blue-100">
        <h1>conteudo page</h1>
      </div>
    </>
  );
}
