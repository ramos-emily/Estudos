public class Produto {
    String nome;
    double preco;

    public Produto(String nome, double preco) {
        this.nome = nome;
        this.preco = preco;
    }

    public void exibirInfo() {
        System.out.println("Produto: " + nome + " Preco: R$ " + preco);
    }

    public void desconto(double percentual) {
        preco = preco - (preco * percentual / 100);
    }
}
