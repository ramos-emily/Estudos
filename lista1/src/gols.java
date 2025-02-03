import java.util.Scanner;

public class gols {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("digite a quantidade de gols do corintians: ");
        int gols1 = scanner.nextInt();
        int corintia = gols1;

        System.out.print("digite a quantidade de gols da Ponte preta:  ");
        int gols2 = scanner.nextInt();
        int ponte = gols2;

        if (corintia < ponte){
            System.out.println("macaca ganhouuuuu");
        } else if (corintia == ponte) {
            System.out.println("empatou vei");
        }else {
            System.out.println("vaii corintiaa");
        }
    }
}



//Exercício 03:
//
//        FUP que peça a quantidade de gols de um timeA e de um timeB em um jogo qualquer.
//        Ao final, mostre quem venceu ou se houve empate baseado na quantidade de gols de cada time.
