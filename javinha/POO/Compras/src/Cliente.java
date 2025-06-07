public class Cliente {
    String nome;
    String email;

    public Cliente(String nome, String email) {
        this.nome = nome;
        this.email = email;
    }

    public void Dados(){
        System.out.println("Cliente: " + nome);
        System.out.println("Email: " + email);
    }
}
