export default function TopBar(){
    return(
        <div className="flex items-center justify-between h-12 fixed bg-gradient-to-r from-blue-200 to-blue-300 w-full">
            <img className="w-5 h-5 ml-40" src="Search.png" alt="" />
            <img className="mr-10 w-7 h-7" src="person.png" alt="icon person login" />
        </div>
    );
}