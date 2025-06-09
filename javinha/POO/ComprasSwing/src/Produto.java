class Produto {
    String nome;
    double preco;

    Produto(String nome, double preco) {
        this.nome = nome;
        this.preco = preco;
    }

    void desconto(double percentual) {
        preco = preco - (preco * percentual / 100);
    }
}
