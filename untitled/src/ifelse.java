public class ifelse {

    public static void main(String[] args) {

    double media = 7.1;
    int faltas = 20;
    boolean postura = true;
    String situacao;

    //estrutura condicional if-else que avalia a situacao do aluno com base na media, faltas e postura
    //se a media for maior ou igual a 5, o numero de faltas for menor que 25 a postura for positiva

    if (media >= 5.0 && faltas < 25 && postura == true){
        situacao = "Passouuuuuuuuuuu";
    }

    else if(media < 5.0 && faltas < 25 && postura){
        situacao = "vai passar o natal na escola bestao";
    }
    else if (media < 5.0 && faltas < 25 && postura){
        situacao = "nao passou ";
    }
    else if (media < 5.0 && faltas < 25 && postura == false){
        situacao = "chamar pra conversar";
    }
    else {
        situacao = "Reprovado";
    }
        System.out.println(situacao);

    }
}
