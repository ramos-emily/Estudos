public class ClasseString {


    // Códigos ANSI para as cores da fonte
    public static final String RESET = "\033[0m";      // Resetando as cores
    public static final String VERMELHO = "\033[31m";   // Vermelho
    public static final String VERDE = "\033[32m";      // Verde
    public static final String AMARELO = "\033[33m";    // Amarelo
    public static final String AZUL = "\033[34m";       // Azul
    public static final String ROXO = "\033[35m";       // Roxo
    public static final String CIANO = "\033[36m";      // Ciano
    public static final String BRANCO = "\033[37m";     // Branco

    // Códigos ANSI para as cores de fundo
    public static final String FUNDO_VERMELHO = "\033[41m";   // Fundo Vermelho
    public static final String FUNDO_VERDE = "\033[42m";      // Fundo Verde
    public static final String FUNDO_AMARELO = "\033[43m";    // Fundo Amarelo
    public static final String FUNDO_AZUL = "\033[44m";       // Fundo Azul
    public static final String FUNDO_ROXO = "\033[45m";       // Fundo Roxo
    public static final String FUNDO_CIANO = "\033[46m";      // Fundo Ciano
    public static final String FUNDO_BRANCO = "\033[47m";     // Fundo Branco



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

//        Trabalhando com String
        String texto = "java é uma linguagem poderosa!";

//        usando o método charAt para acessar um caractere espesifico
        char caractere = texto.charAt((5));
        System.out.println("Caractere na posição 5: " + caractere);

        boolean comecaComPoderosa = texto.startsWith(("Java"));
        System.out.println("A string começa com 'Poderosa!'? " + comecaComPoderosa );

        boolean terminaComPoderosa = texto.endsWith("poderosa!");
        System.out.println("A string termina com 'poderosa!'?" + terminaComPoderosa);

        //convertendo string para letras maiusculas com toUpperCase
        String textoMaiusculo = texto.toUpperCase();
        System.out.println("Texto em maiuscula: " + textoMaiusculo);

        //convertendo string para letras minusculas com toLowerCase

        String textoMinusculo = texto.toLowerCase();
        System.out.println("Texto em minusculas: " + textoMinusculo);

        //usando o equals para comparar Strings
        String textoComparar = "Java é uma linguagem poderosa!";
        boolean saoIguais = texto.equals(textoComparar); // verifica se os dois textos sao iguais
        System.out.println("as duas Strings sao iguais? " + saoIguais);

        //usando a concatenaçao de string
        String concatenado = texto + "" + textoComparar;
        System.out.println(VERMELHO + "texto concatenado: " + RESET + concatenado);

        System.out.println(VERMELHO + "Deus tenha piedade dessa pobre alma " + RESET );
        System.out.println(FUNDO_ROXO + "amo minha vida, gratidao" + RESET);
        System.out.println(FUNDO_VERMELHO + AZUL + "aaaaaaaaaaaaaa" + RESET); //resert mantem o fundo do tamanho da frase

        // Usando as cores ANSI para formatar o texto
//        System.out.println(VERMELHO + "Texto em Vermelho!" + RESET);
//        System.out.println(VERDE + "Texto em Verde!" + RESET);
//        System.out.println(AMARELO + "Texto em Amarelo!" + RESET);
//        System.out.println(AZUL + "Texto em Azul!" + RESET);
//        System.out.println(ROXO + "Texto em Roxo!" + RESET);
//        System.out.println(CIANO + "Texto em Ciano!" + RESET);
//        System.out.println(BRANCO + "Texto em Branco!" + RESET);
//
//        // Usando cores de fundo
//        System.out.println(FUNDO_VERMELHO + "Texto com Fundo Vermelho!" + RESET);
//        System.out.println(FUNDO_VERDE + "Texto com Fundo Verde!" + RESET);
//        System.out.println(FUNDO_AMARELO + "Texto com Fundo Amarelo!" + RESET);
//        System.out.println(FUNDO_AZUL + "Texto com Fundo Azul!" + RESET);
//        System.out.println(FUNDO_ROXO + "Texto com Fundo Roxo!" + RESET);
//        System.out.println(FUNDO_CIANO + "Texto com Fundo Ciano!" + RESET);
//        System.out.println(FUNDO_BRANCO + "Texto com Fundo Branco!" + RESET);



    }

}
