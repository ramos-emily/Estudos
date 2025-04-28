package Try_catch;

import java.util.Scanner;

public class TryCatchEntrada {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        try {
            System.out.print("Digite o numerador: ");
            int numerador = scanner.nextInt();


            System.out.print("Digite o denominador: ");
            int denominador = scanner.nextInt();

            int result = dividir(numerador, denominador);
            System.out.println("Result: " + result);

        } catch (ArithmeticException e) { //erro de calculo
            System.out.println("Erro: nao é possivel dividir por zero.");
        } catch (Exception e) { //erro de entrada
            System.out.println("Error: Entrada inválida. Certifique-se de inserir numeros inteiros. ");
        } finally {
            scanner.close();
            System.out.println("Programa finalizado! ");
        }
    }

        public static int dividir(int a, int b){
            return a / b;
    }

}

