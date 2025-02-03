import java.util.Scanner;

public class cadastro {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite seu nome e sobrenome: ");
        String name = scanner.next();

        System.out.println("Digite o ano de nascimento: ");
        int date = scanner.nextInt();

        System.out.println("Qual a sua pretençção salarial?: ");
        int salario = scanner.nextInt();

        System.out.println("Grau de escolaridade: ");
        String escolar = scanner.next();

        System.out.println("Cargo pretendido: ");
        String cargo = scanner.next();

        System.out.println("Possui CNH do tipo B? s/n: ");
        String cnh = scanner.next();

        System.out.println("-----DADOS DO CANDIDATO-----");
        System.out.printf(name);
        System.out.println(date);
        System.out.println(salario);
        System.out.println(escolar);
        System.out.println(cargo);
        System.out.println(cnh);
    }
}
