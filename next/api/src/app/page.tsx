
export async function Home() {

  const data = await fetch('https://pokeapi.co/api/v2/pokemon/ditto')

  const todos = await data.json()

  console.log(todos)

  return (
    <div>
    </div>
  );
}
