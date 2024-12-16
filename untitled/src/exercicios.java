
import java.util.Scanner;

public class exercicios {
    public static void main(String[] args){

        Scanner  scanner= new Scanner(System.in);
        System.out.print("digite sua altura: ");
        float altura = scanner.nextFloat();

        System.out.print("digite seu peso: ");
        float peso = scanner.nextFloat();

        float imc = peso/(altura*altura);

        System.out.printf("seu IMC é de: %.2f%n", imc); //tem q ser assim %.2f%n

        scanner.close();

    }

}

//conversao de fah para celsius

//        Scanner scanner = new Scanner(System.in);
//
//        System.out.print("digite a temperatura: ");
//        float fah = scanner.nextFloat();
//
//        float cel = (fah - 32) / 1.8f;
//
//        System.out.printf("a temperatura é: %.2f%n", cel);
//
//        scanner.close();


//conversao de celsius para fah

//Scanner scanner = new Scanner(System.in);
//
//        System.out.print("digite a temperatura: ");
//                float cel = scanner.nextFloat();
//
//                float fah = cel * 1.8f + 32;
//
//                System.out.printf("a temperatura é: %.2f%n", fah);
//
//                scanner.close();
