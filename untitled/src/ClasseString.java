public class ClasseString {

    public static void main(String[] args){

        //exemplificando com operadores logicos:
        boolean condicao1 = true;
        boolean condicao2 = false;

        //operadores logicos
            System.out.println("Resultado do operador AND (&&): " + (condicao1 && condicao2)); //falso
            System.out.println("Resultado de operador OR (||): " + (condicao1 || condicao2)); //true
            System.out.println("Resultado de operador NOT (!): " + !condicao1); //false

        //operadores de incremento e decremento
            int num = 10;


        //incremento (pós-fixado)
            num++; //incremento pós fixado
            System.out.println("incremento pós fixado: " + num);


        //decremento (pós-fixado)
        num--; //decremento pós-fixado
        System.out.println("decremento pós fixado: " + num);

        //operados de incremento e decremento pré-fixado
        System.out.println("incremento pré-fixado" + ++num);
        System.out.println("decremento pré-fixado" + --num);

        //operador ternario
        String result = (num > 5) ? "maior que 5: " : "menor igual a 5";
        System.out.println("resultado do operador ternario: " + result);


    }

}
