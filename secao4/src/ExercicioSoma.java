import java.util.Scanner;

public class ExercicioSoma {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("digite um numero: ");
        int numberOne = scanner.nextInt();

        System.out.println("digite outro numero: ");
        int numberTwo = scanner.nextInt();

        int soma = numberOne + numberTwo;
        System.out.println("a soma é: "+ soma);

        scanner.close();
    }
}