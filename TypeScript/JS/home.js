fetch("https://dummyjson.com/products")
  .then((res) => res.json())
  .then((res) => {
    const cardContainer = document.getElementById("card-container");

    res.products.map((produto) => {
      const card = document.createElement("div");
      card.className = "card";
      cardContainer.append(card);

      const productid = document.createElement("button");
      productid.className = "product-id";
      productid.id = `product-${produto.id}`;
      productid.innerHTML = "VISUALIZAR";
      productid.addEventListener("click", () => {
        redirect(produto.id);
      });

      const image = document.createElement("img");
      image.src = produto.images[0];
      image.alt = "imagem";

      const titulo = document.createElement("h2");
      titulo.innerHTML = produto.title;

      const preco = document.createElement("h3");
      preco.innerHTML = produto.price;

      card.append(image, titulo, preco, productid);
    });
  });

function redirect(id) {
  window.location.href = `produto.html?id=${id}`;
}

const urlParams = new URLSearchParams(window.location.search);
const productId = urlParams.get("id");

fetch(`https://dummyjson.com/products/${productId}`)
  .then((res) => res.json())
  .then((produto) => {
    const container = document.getElementById("produto");

    const image = document.createElement("img");
    image.src = produto.images[0];
    image.alt = produto.title;

    const titulo = document.createElement("h2");
    titulo.textContent = produto.title;

    const preco = document.createElement("h3");
    preco.textContent = `Preço: $${produto.price}`;

    const descricao = document.createElement("p");
    descricao.textContent = produto.description;

    container.append(image, titulo, preco, descricao);
  });
