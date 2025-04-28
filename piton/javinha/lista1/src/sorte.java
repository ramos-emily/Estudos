import java.util.*;

public class sorte {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        System.out.println("..............Sorteador..............");
        System.out.println("Escolha um numero de 1 a 100: ");
        int querochorar = scanner.nextInt();

        Random gerador = new Random();
        int affveir = gerador.nextInt(100)+1;
        System.out.println("o numero é " + affveir);

        if (querochorar == affveir){
            System.out.println("Voce acertou vei que sorte");
        }else {
            System.out.println("errou, obivio");
        }
    }
}
