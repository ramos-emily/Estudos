//FUP que peça ao usuário uma idade e mostre na tela em qual categoria a pessoa se encaixa, de acordo com a tabela abaixo:



import java.util.Scanner;

public class FaixaEtaria {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("digite sua idade: ");
        int idade = scanner.nextInt();
        int anos = idade;

    if (anos <= 14 && anos >= 1){
        System.out.println("criancinha owwnnn");
    } else if (anos >= 15 && anos <= 17) {
        System.out.println("Adolecente insuportavel que nao sabe nada da vida e fica atrapalhando a vida dos outros");
    } else if (anos >=18 && anos <= 30) {
        System.out.println("jovem senhor");
    } else if (anos <= 0) {
        System.out.println("nasce primeiro porra");
    } else if (anos >= 31 && anos <= 59) {
        System.out.println("Adulto chato");
    } else {
        System.out.println("Velho insuportavel");
    }

    }
}




