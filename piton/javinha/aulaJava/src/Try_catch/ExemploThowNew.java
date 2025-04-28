package Try_catch;

import java.util.Scanner;

public class ExemploThowNew {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        try {
            System.out.println("Digite sua idade: ");
            int age = scanner.nextInt();

            if (age < 18){
                throw new IllegalArgumentException("Error: idade minima é 18 anos");

            }
            System.out.println("Cadastro realizado! ");
        }catch (IllegalArgumentException e){
            System.out.println("Exceção capturada: " + e.getMessage());

        }finally {
            scanner.close();
            System.out.println("Programa finalizado");
        }

    }

}
