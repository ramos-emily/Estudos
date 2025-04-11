import java.util.Scanner;

public class gameName {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("quantos? ");
        int quant = sc.nextInt();
        sc.nextLine();

        String[] names = new String[quant];

        for (int i = 0; i < quant; i++){
            System.out.println("name do number" + (i + 1) + " : ");
            names[i] = sc.nextLine();
        }

    }
}
