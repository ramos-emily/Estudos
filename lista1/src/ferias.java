import java.util.Scanner;

public class ferias {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("---------------------lista de viagens---------------------");
        System.out.print("[1]Maceió\n[2]Porto de galinhas\nOnde vc pretende passar as ferias?:\n");
        int onde = scanner.nextInt();

        System.out.print("[1]sim\n[2]nao\nvoce deseja o valor com almoço/janta incluso?:\n");
        int sn = scanner.nextInt();

        int base = 3000;

        if (onde == 1 && sn == 1){
            System.out.printf("O valor da sua viagem é de: %d", base);
        } else if (onde == 1 && sn ==2) {
            int desconto = 85;
            int porcentagem = base * desconto / 100;
            System.out.printf("O valor da sua viagem é de: %d", porcentagem);
        } else if (onde == 2 && sn == 1) {
            int desconto = 60;
            int porcentagem = base * desconto / 100;
            System.out.printf("O valor da sua viagem é de: %d", porcentagem);
        } else if (onde == 2 && sn == 2) {
            int desconto = 45;
            int porcentagem = base * desconto / 100;
            System.out.printf("O valor da sua viagem é de: %d", porcentagem);
        }
    }
}
















// que pergunte ao usuário onde ele pretende passar suas férias. Além disso,
// o programa deve perguntar se ele deseja o valor com almoço/janta incluso ou não e mostrar o valor final da viagem na tela.
// O valor base de cálculo para todas as viagens é de R$3000,00.(Atente-se aos códigos/números que deverão ser usados para fazer as condições no programa):