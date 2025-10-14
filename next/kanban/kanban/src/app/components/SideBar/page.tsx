export default function SideBar(){
    return(
        <>
        <div className="fixed inset-y-0 left-0 bg-white w-30">
            <h1 className="flex items-center justify-center text-xl h-12 bg-blue-400 text-white font-bold ">Events</h1>
            <ul className="flex flex-col">
                <li className="flex flex-col justify-center items-center py-4">
                    <img src="exam.png" alt="" />
                    <h1>aaaaaaa</h1>
                </li>
                <li className="flex flex-col justify-center items-center">
                    <img src="cart.png" alt="" />
                    <h1>bbbbbbb</h1>
                </li>
                <li className="flex flex-col justify-center items-center py-4">
                    <img src="trash.png" alt="" />
                    <h1>cccccccc</h1>
                </li>
                <li className="mt-auto mb-10 flex flex-col justify-center items-center py-4">
                    <img src="sett.png" alt="" />
                    <h1>aaaaaaaa</h1>
                </li>
                
            </ul>
        </div>
        </>
    );
}