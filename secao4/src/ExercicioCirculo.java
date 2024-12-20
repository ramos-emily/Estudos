//Faça um programa para ler o valor do raio de um círculo, e depois mostrar o valor da área deste círculo com quatro
//casas decimais conforme exemplos.
//Fórmula da área: area = π . raio2
//Considere o valor de π = 3.14159
//Entrada: Saída:
//        2.00 A=12.5664
//        Entrada: Saída:
//        100.64 A=31819.3103
//        Entrada: Saída:
//        150.00 A=70685.7750

import java.util.Scanner;
public class ExercicioCirculo {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("digite o valor do raio: ");
        int raio = scanner.nextInt();

        double pi = 3.14;
        double area = pi * Math.pow(raio, 2);

        System.out.printf("a area do circulo com raio %d é: %.2f", raio, area);

        scanner.close();

    }
}
