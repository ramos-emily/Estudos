//Fazer um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e
//        mostre:
//        a) a área do triângulo retângulo que tem A por base e C por altura.
//        b) a área do círculo de raio C. (pi = 3.14159)
//        c) a área do trapézio que tem A e B por bases e C por altura.
//        d) a área do quadrado que tem lado B.
//        e) a área do retângulo que tem lados A e B.
//        Exemplos:
//        Entrada: Saída:
//        3.0 4.0 5.2 TRIANGULO: 7.800
//        CIRCULO: 84.949
//        TRAPEZIO: 18.200
//        QUADRADO: 16.000
//        RETANGULO: 12.000
//        Entrada: Saída:
//        12.7 10.4 15.2 TRIANGULO: 96.520
//        CIRCULO: 725.833
//        TRAPEZIO: 175.560
//        QUADRADO: 108.160
//        RETANGULO: 132.080



import java.util.Scanner;

public class geometrica {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite os valores de A, B e C: ");
        double A = scanner.nextDouble();
        double B = scanner.nextDouble();
        double C = scanner.nextDouble();

        double areaTriangulo = (A * C) / 2; // Área do triângulo
        double pi = 3.14159;
        double areaCirculo = pi * Math.pow(C, 2); // Área do círculo
        double areaTrapezio = ((A + B) * C) / 2; // Área do trapézio
        double areaQuadrado = Math.pow(B, 2); // Área do quadrado
        double areaRetangulo = A * B; // Área do retângulo

        System.out.printf("TRIANGULO: %.3f%n", areaTriangulo);
        System.out.printf("CIRCULO: %.3f%n", areaCirculo);
        System.out.printf("TRAPEZIO: %.3f%n", areaTrapezio);
        System.out.printf("QUADRADO: %.3f%n", areaQuadrado);
        System.out.printf("RETANGULO: %.3f%n", areaRetangulo);

        scanner.close();
    }

}
