public class Carrinho {
    Produto[] produtos = new Produto[10];
    int[] quantidades = new int[10];
    int tamanho = 0;

    public void addProduto(Produto p, int quantidade) {
        produtos[tamanho] = p;
        quantidades[tamanho] = quantidade;
        tamanho++;
    }

    public double Total() {
        double total = 0;
        for (int i =0; i < tamanho; i++){
            total += produtos[i].preco * quantidades[i];
        }
        return total;
    }

    public void Resumo() {
        System.out.println("Resumo do Carrinho:");
        for (int i = 0; i < tamanho; i++) {
            System.out.println("- " + produtos[i].nome + " Preco: R$ " + produtos[i].preco + " Quantidade" + quantidades[i]);
        }
        System.out.println("Total: " + Total());
    }


    public void rmProduto(String nome) {
        for (int i = 0; i < tamanho; i++) {
            if (produtos[i].nome.equalsIgnoreCase(nome)) {
                for (int j = i; j < tamanho - 1; j++) {
                    produtos[j] = produtos[j + 1];
                    quantidades[j] = quantidades[j + 1];
                }
                tamanho--;
                System.out.println("Produto \"" + nome + "\" removido.");
                return;
            }
        }
        System.out.println("Produto \"" + nome + "\" não encontrado.");
    }
}
