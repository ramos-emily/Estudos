public class opAri {

    public static void main(String[] args) { //tsv atalho

        int a = 10;
        int b = 5;
        double x = 7.5;
        double y = 3.2;

        //adição
        int somaInt = a + b;
        double somaDec = x+ y;
        System.out.println("Soma de inteiros: " + somaInt);
        System.out.println("soma de decimais: " + somaDec);

        //subtraçao
        int subInt = a - b;
        double subDec = x - y;
        System.out.println("subtração de inteiros: " + subInt);
        System.out.println("subtração de decimais: " + subDec);

        //multiplicaçao
        int mulInt = a * b;
        double mulDec = x * y;
        System.out.println("multiplicação de inteiros: " + mulInt);
        System.out.println("multiplicação de decimais: " + mulDec);

        //divisao
        int divInt = a / b;
        double dibDec = x / y;
        System.out.println("divisao de inteiros: " + divInt);
        System.out.println("divisao de decimais: " + dibDec);

        //modulo (%)
        int modInt = a%b;
        double modDec = x % y;
        System.out.println("modulo de inteiros: " + modInt);
        System.out.println("modulo de decimais: " + modDec);

        //incremento(++)
        int incremento = a;
        incremento++;
        System.out.println("incremento de a: " + incremento);

        //decremento(--)
        int decremento = a;
        decremento--;
        System.out.println("decremento de a: " + decremento);

        //exem de expressao de mult operadores
        double resultComplexo = (x * y) * (a - b)/2;
        System.out.println("resultado complexo de expressao: " + resultComplexo);


    }


}
