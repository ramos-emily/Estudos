fetch('https://dummyjson.com/products')
    .then((res) => res.json())
    .then((res) => {
        const cardContainer = document.getElementById("card-container")
        
        res.products.map((produto) => {
            const card = document.createElement('div');
            card.className = "card";
            cardContainer.append(card);

            const image = document.createElement('img');
            image.src = produto.images[0];
            image.alt = "Imagem";
            card.append(image);

            const title = document.createElement('h2');
            title.innerHTML = produto.title;
            card.append(title);

            const price = document.createElement('h3');
            price.innerHTML = produto.price
            card.append(price);
        })
    });  