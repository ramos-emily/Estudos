import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {


        String[] nomeArr = new String[10];
        //arraylist
        ArrayList<String> caraio = new ArrayList<>(); //pra usar isso precisa do " import java.util.ArrayList;  "
        caraio.add("gaibriel");
        caraio.add("july");
        caraio.add("carol");

        System.out.println(caraio.get(0));

        caraio.remove(0);

        System.out.println(caraio.get(0));

    }
}


/*
        //condicionais
        boolean bool = false;
        String help = "";
        //.isBlank(), se a str é vazia
        if (help .isBlank()) {
            System.out.println("aaaaaaaaaaaaaa");
        } else {
            System.out.println("morte");
        }

        //vetor
        int[] cole = {1, 2, 3, 4, 5};
        System.out.println(cole[2]);
        .length acessa a ultima posição do array


        //arraylist
        ArrayList<String> caraio = new ArrayList<>(); //pra usar isso precisa do " import java.util.ArrayList;  "
        caraio.add("gaibriel");
        caraio.add("july");
        caraio.add("carol");

        System.out.println(caraio.get(0));

        caraio.remove(0);

        System.out.println(caraio.get(0));
        System.out.println("Hello World! ");

                //inteiros
        //byte => 8 bits => -128 a 127
            byte varMy = 100;
        //short => 16 bits => -32,768 a 32,767
            short varMi = 10;
        //int => 32 bits => -2.147.483.648 a 2.147.483.647
            int varAi = 10000;
        // long => 64 bits => -9.223.372.036.854.775.808 a 9.223.372.036.854.775.807
            long varOMG = 10000000;    termina com L

                //decimais
        //float => 32 bits => poucos numeros apos a virgula         termina com "f"
        //double => 64 bits> mais numeros

                //palavras
        //String => palavras e frases
        //char => unico caractere => a, b, c, d (aspas simples!!!)
            char varCaraio = 'a';

        //boolean => true or false

    }
}
*/