import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int [] num = {1, 2, 3, 10, 7};

        Arrays.sort(num);

        System.out.println("Array ordenado: " + Arrays.toString(num));

    }
}