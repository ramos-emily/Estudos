import java.util.Scanner;

public class compra {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("digite o valor unitario de um produto: ");

        double caralho = scanner.nextInt();
        double unitario = caralho;


        System.out.println("digite a quantidade que deseja: ");

        double funcionaporfavor = scanner.nextInt();
        double quant = funcionaporfavor;
        double total = unitario * quant ;
        double desconto = total * 0.90;

        if (quant <= 12 && quant >=1 ){
            System.out.printf("o valor total foi de: %2f"  ,total);
        } else if (quant >=13){
            System.out.printf("o valor final com desconto foi de: %2f" ,desconto);
        }
    }
}






//    que pergunte ao usuário o valor unitário de um produto e a quantidade que ele quer comprar desse produto.
//    Se a quantidade que ele deseja for até 12 unidades, o valor do produto é o valor unitário normal vezes a quantidade.
//    Se ele deseja comprar mais do que 12 unidades, o valor unitário do produto terá o desconto de 10%,ou, o valor total da compra.
//    Mostre na tela o valor total da compra, baseado nessas condições.
