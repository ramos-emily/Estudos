import java.util.Scanner;

public class compra {
    public compra() {
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("digite o valor unitario de um produto: ");
        double tabom = (double)scanner.nextInt();
        System.out.println("digite a quantidade que deseja: ");
        double funcionaporfavor = (double)scanner.nextInt();
        double total = tabom * funcionaporfavor;
        double desconto = total * 0.9;
        if (funcionaporfavor <= 12.0 && funcionaporfavor >= 1.0) {
            System.out.printf("o valor total foi de: %2f", total);
        } else if (funcionaporfavor >= 13.0) {
            System.out.printf("o valor final com desconto foi de: %2f", desconto);
        }
    }
}