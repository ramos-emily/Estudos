public class Garagem {
    public static void main(String[] args) {

        Carro mycar = new Carro("Vermelho", "ford", "Mustang");
        System.out.println("foi vei, criou objeto.");

        mycar.exibirInfo();
        mycar.ligar();
        mycar.acelerar(50);
        mycar.frear(20);
        mycar.desligar();
        System.out.println();

        Carro gaibrielCar = new Carro("Azul", "Chevrolet", "Camaro");
        System.out.println("carringo do gaibriel");

        mycar.exibirInfo();
        mycar.ligar();
        mycar.acelerar(80);
        mycar.acelerar(30);
        mycar.frear(100);
        mycar.desligar();
        System.out.println();

    }
}
