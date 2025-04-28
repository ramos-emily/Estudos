import java.util.Scanner;

public class questions {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("---------Quiz---------");
        System.out.println("qual a minha comida preferida?: ");
        System.out.println("---------Alternativas---------");
        System.out.println("[1]lasanha\n[2]batata\n[3]sorvete");
        System.out.print("Resposta: ");
        int comida = scanner.nextInt();
        if (comida == 2){
            System.out.println("Voce me conhece msm veir\n");
        }else {
            System.out.println("fraude!!!!\n");
        }
        System.out.println("o que eu odeio?:\n ");
        System.out.println("---------Alternativas---------");
        System.out.println("[1]Gaibriel\n[2]Acordar cedo\n[3]Codar");
        System.out.print("Resposta: ");
        int odioSupremo = scanner.nextInt();
        if (odioSupremo == 1){
            System.out.println("Sim, isso mesmo");
        }else {
            System.out.println("nao veir");
        }
    }
}
