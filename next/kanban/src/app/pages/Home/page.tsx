export default function Conteudo(){
    return(
        <>
        <div className="ml-30 bg-purple-200 min-w-full min-h-screen flex flex-col">
            <div className="flex flex-row">
                <h1 className="mt-20 ml-10 text-3xl font-bold">Studio Board</h1>
                <button className="mt-20 ml-5 -rotate-270 "> &gt; </button>
            </div>
            <div className="grid grid-cols-4 gap-5 my-10 ml-10">
                <div className="bg-gray-100 p-3 flex justify-between">
                    <h4 className="flex justify-between items-center">Backlog</h4>
                    <button className=" -rotate-270">...</button>
                </div>
            </div>
        </div>
        </>
    )
}