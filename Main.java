import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        //inicializando scanner para receber entradas do usuario
        Scanner batatinhaFrita = new Scanner(System.in);


        //tipos de dados primitivos
        int idade = 25;
        double altura = 1.75;
        char inicial = 'a';
        boolean estudante = true;

        //demonstrando diferentes tipos de saída
        System.out.println("ex de saida");
        System.out.println("blablabla");

        System.out.println();

        //usando printf para formatação de Str
        //%d é usado para identificar inteiros
        //%2f usado para duas casas decimais
        //%c é usado para caracteres

        System.out.printf("minha idade é %d anos, miha altura é %.2f m e minha inicial é %c.\n", idade, altura, inicial);



    }
}