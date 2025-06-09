import javax.swing.*;
import java.awt.event.*;
import java.util.ArrayList;

// Criei uma classe chamada CarrinhoSwing que é uma janela (JFrame).
public class CarrinhoSwing extends JFrame {

    // Aqui estão os campos de texto onde vou digitar os dados do cliente e dos produtos.
    private JTextField nomeClienteField, emailField;
    private JTextField nomeProdutoField, precoProdutoField, qtdProdutoField;

    // Área onde mostro o conteúdo do carrinho.
    private JTextArea carrinhoArea;

    // Duas listas: uma para guardar os produtos, outra para guardar as quantidades deles.
    private ArrayList<Produto> produtos = new ArrayList<>();
    private ArrayList<Integer> quantidades = new ArrayList<>();

    // Construtor da classe. Aqui eu monto toda a interface da janela.
    public CarrinhoSwing() {
        setTitle("Carrinho de Compras"); // Título da janela
        setSize(400, 650); // Tamanho da janela
        setLayout(null); // Layout manual para posicionar os elementos

        // Criei e posicionei o rótulo para a parte do cliente
        JLabel clienteLabel = new JLabel("Cliente:");
        clienteLabel.setBounds(10, 10, 100, 25);
        add(clienteLabel);

        // Campos para o nome e email do cliente
        nomeClienteField = new JTextField("Nome");
        emailField = new JTextField("Email");
        nomeClienteField.setBounds(10, 40, 150, 25);
        emailField.setBounds(170, 40, 200, 25);
        add(nomeClienteField);
        add(emailField);

        // Rótulo da seção de produtos
        JLabel produtoLabel = new JLabel("Adicionar Produto:");
        produtoLabel.setBounds(10, 80, 200, 25);
        add(produtoLabel);

        // Campos para nome, preço e quantidade do produto
        nomeProdutoField = new JTextField("Nome Produto");
        precoProdutoField = new JTextField("Preço");
        qtdProdutoField = new JTextField("Qtd");

        nomeProdutoField.setBounds(10, 110, 150, 25);
        precoProdutoField.setBounds(170, 110, 80, 25);
        qtdProdutoField.setBounds(260, 110, 50, 25);

        add(nomeProdutoField);
        add(precoProdutoField);
        add(qtdProdutoField);

        // Botão para adicionar o produto no carrinho
        JButton addProdutoBtn = new JButton("Adicionar");
        addProdutoBtn.setBounds(10, 150, 150, 30);
        add(addProdutoBtn);

        // Área onde mostro os produtos adicionados e o total
        carrinhoArea = new JTextArea();
        carrinhoArea.setBounds(10, 200, 360, 300);
        carrinhoArea.setEditable(false); // Só leitura
        add(carrinhoArea);

        // Botões para mostrar carrinho, aplicar desconto e remover produto
        JButton mostrarCarrinhoBtn = new JButton("Mostrar Carrinho");
        mostrarCarrinhoBtn.setBounds(10, 510, 150, 30);
        add(mostrarCarrinhoBtn);

        JButton descontoBtn = new JButton("10% Desconto 1º Produto");
        descontoBtn.setBounds(170, 510, 200, 30);
        add(descontoBtn);

        JButton removerProdutoBtn = new JButton("Remover Produto");
        removerProdutoBtn.setBounds(10, 550, 360, 30);
        add(removerProdutoBtn);

        // Aqui eu conecto os botões com suas funções
        addProdutoBtn.addActionListener(e -> adicionarProduto());
        mostrarCarrinhoBtn.addActionListener(e -> mostrarCarrinho());
        descontoBtn.addActionListener(e -> desconto());
        removerProdutoBtn.addActionListener(e -> removerProduto());

        // Por fim, deixo a janela visível
        setVisible(true);
    }

    // Função para adicionar um produto à lista
    private void adicionarProduto() {
        try {
            String nome = nomeProdutoField.getText();
            double preco = Double.parseDouble(precoProdutoField.getText());
            int qtd = Integer.parseInt(qtdProdutoField.getText());

            produtos.add(new Produto(nome, preco)); // adiciona o produto
            quantidades.add(qtd); // adiciona a quantidade correspondente
            JOptionPane.showMessageDialog(this, "Produto adicionado!");
        } catch (NumberFormatException e) {
            JOptionPane.showMessageDialog(this, "Erro: Preço ou quantidade inválida.");
        }
    }

    // Mostra o resumo do carrinho: nome, preço, quantidade e total
    private void mostrarCarrinho() {
        carrinhoArea.setText(""); // limpa o texto atual
        double total = 0;

        for (int i = 0; i < produtos.size(); i++) {
            Produto p = produtos.get(i);
            int q = quantidades.get(i);
            double subtotal = p.preco * q;

            carrinhoArea.append(p.nome + " | R$" + p.preco + " x " + q + " = R$" + subtotal + "\n");
            total += subtotal;
        }

        carrinhoArea.append("\nTOTAL: R$" + total);
    }

    // Aplica 10% de desconto no primeiro produto da lista
    private void desconto() {
        if (!produtos.isEmpty()) {
            produtos.get(0).desconto(10); // chama o método de desconto da classe Produto
            JOptionPane.showMessageDialog(this, "Desconto de 10% aplicado ao primeiro produto!");
        } else {
            JOptionPane.showMessageDialog(this, "Nenhum produto no carrinho.");
        }
    }

    // Remove um produto do carrinho, buscando pelo nome
    private void removerProduto() {
        String nomeParaRemover = JOptionPane.showInputDialog(this, "Digite o nome do produto a remover:");

        if (nomeParaRemover == null || nomeParaRemover.trim().isEmpty()) {
            return;
        }

        for (int i = 0; i < produtos.size(); i++) {
            if (produtos.get(i).nome.equalsIgnoreCase(nomeParaRemover.trim())) {
                produtos.remove(i);
                quantidades.remove(i);
                JOptionPane.showMessageDialog(this, "Produto removido com sucesso!");
                return;
            }
        }

        JOptionPane.showMessageDialog(this, "Produto não encontrado.");
    }

    // Método principal. Aqui é onde o programa começa de verdade.
    public static void main(String[] args) {
        new CarrinhoSwing(); // cria e mostra a janela
    }
}
