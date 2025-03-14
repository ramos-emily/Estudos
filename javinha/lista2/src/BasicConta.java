import java.util.Scanner;

public class BasicConta {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("digite um numero: ");
        int num1 = scanner.nextInt();

        System.out.println("Digite outro numero: ");
        int num2 = scanner.nextInt();

        int soma = num1 + num2;
        int sub = num1 - num2;
        int mult = num1 * num2;
        int div = num1 / num2;
        int elev = num1 ^ num2;
        int resto = num1 % num2;


        System.out.printf("A soma deles é: %d", soma );
        System.out.printf("\nA subtração deles é: %d", sub);
        System.out.printf("\nA multiplicação deles é: %d", mult);
        System.out.printf("\nA divisão dele é: %d", div);
        System.out.printf("\nO primeiro numero elevado pelo segundo é: %d", elev);
        System.out.printf("\nO resto da divisao é: %d", resto);

        if (div <= 0){
            System.out.println("precisa ser um numero maior que zero!");
        }
    }
}