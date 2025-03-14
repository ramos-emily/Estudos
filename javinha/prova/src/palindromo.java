import java.util.Scanner;

public class palindromo {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("digite uma palavra: ");
        String palavra = scanner.nextLine();
        System.out.println(palavra);
        reverso = new StringBuilder().reverse().toString();
        System.out.print(reverso);


        scanner.close();
    }

}


//
//Objetivo: Escrever um programa que verifique se uma palavra fornecida pelo usuário é um palíndromo (uma palavra que pode ser lida de trás para frente da mesma forma, como "arara").
//        Desafio: Você pode inverter a palavra e comparar com a original, ignorando maiúsculas e minúsculas.
