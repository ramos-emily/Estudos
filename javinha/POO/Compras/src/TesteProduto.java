import java.util.Scanner;

public class TesteProduto {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Criar cliente
        System.out.print("Digite o nome do cliente: ");
        String nomeCliente = scanner.nextLine();

        System.out.print("Digite o e-mail do cliente: ");
        String emailCliente = scanner.nextLine();

        Cliente cliente = new Cliente(nomeCliente, emailCliente);
        cliente.Dados();

        // Criar carrinho
        Carrinho carrinho = new Carrinho();

        // Adicionar produtos (so 3 mesmo porque sim, o mercado é meu)
        for (int i = 1; i <= 3; i++) {
            System.out.println("\nProduto " + i + ":");
            System.out.print("Nome: ");
            String nomeProduto = scanner.nextLine();

            System.out.print("Preço: ");
            double precoProduto = scanner.nextDouble();

            System.out.print("Quantidade: ");
            int quantidade = scanner.nextInt();
            scanner.nextLine(); // limpar buffer

            Produto produto = new Produto(nomeProduto, precoProduto);
            carrinho.addProduto(produto, quantidade);
        }

        // Mostrar resumo antes do desconto
        System.out.println("\nResumo do carrinho ANTES do desconto:");
        carrinho.Resumo();

        // Aplicar desconto em um produto
        System.out.print("\nDigite o nome do produto para aplicar 10% de desconto: ");
        String nomeDesconto = scanner.nextLine();

        for (int i = 0; i < carrinho.tamanho; i++) {
            if (carrinho.produtos[i].nome.equalsIgnoreCase(nomeDesconto)) {
                carrinho.produtos[i].desconto(10);
                System.out.println("Desconto aplicado!");
                break;
            }
        }

        // Mostrar resumo depois do desconto
        System.out.println("\nResumo do carrinho DEPOIS do desconto:");
        carrinho.Resumo();

        // Remover produto
        System.out.print("\nDigite o nome do produto para remover do carrinho: ");
        String nomeRemover = scanner.nextLine();
        carrinho.rmProduto(nomeRemover);

        // Mostrar carrinho final
        System.out.println("\nCarrinho final:");
        carrinho.Resumo();

        scanner.close();
    }
}