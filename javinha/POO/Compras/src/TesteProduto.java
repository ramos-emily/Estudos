public class TesteProduto {
    public static void main(String[] args) {
        Cliente cliente = new Cliente("João Silva", "joao@email.com");
        cliente.Dados();

        Produto p1 = new Produto("Celular", 1500);
        Produto p2 = new Produto("Carregador", 100);
        Produto p3 = new Produto("Capa de Silicone", 50);

        Carrinho carrinho = new Carrinho();
        carrinho.addProduto(p1, 1);
        carrinho.addProduto(p2, 2);
        carrinho.addProduto(p3, 1);

        System.out.println("\nAntes do desconto:");
        carrinho.Resumo();

        p2.desconto(10);

        System.out.println("\nDepois do desconto de 10% no Carregador:");
        carrinho.Resumo();

        System.out.println("\nRemovendo a Capa de Silicone:");
        carrinho.rmProduto("Capa de Silicone");

        System.out.println("\nCarrinho final:");
        carrinho.Resumo();
    }
}