public class Main {
    public static void main(String[] args) {

        String[] friends = {"Julia", "Caua", "Yasmin", "Carol", "Thalita", "Nicolly", "Renato", "Alisson"};

        int contadorDeA = 0;

        for (int i = 0; i < friends.length; i++){
            String name = friends[i];

            if (name.startsWith("A")){

                contadorDeA++;
            }
        }

        System.out.println("name with (A): "+ contadorDeA);
    }
}
