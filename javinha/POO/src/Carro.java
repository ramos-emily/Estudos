public class Carro {

    String cor;
    String marca;
    String modelo;
    int velocAtual;

    public Carro(String cor, String marca, String modelo){

        this.cor = cor;

        this.marca = marca;

        this.modelo = modelo;

        this.velocAtual = 0;
    }

    public void ligar() {
        System.out.println("bla bla blabla" + this.modelo + "ligou.");
    }

    public void acelerar(int incremento){
        this.velocAtual += incremento;
        System.out.println("bla bla blabla" + this.velocAtual + "KM");
    }

    public void frear(int decremento){
        if (this.velocAtual - decremento >= 0){
            this.velocAtual -= decremento;
            System.out.println("bla bla blabla" + this.velocAtual + "KM");
        }else {
            this.velocAtual = 0;
            System.out.println("paroooowww");
        }
    }
    public void desligar(){
        System.out.println("the car" + this.modelo + "morreu");
    }

    public void exibirInfo(){
        System.out.println("______Info car______");
        System.out.println("marca" + this.marca);
        System.out.println("modelo" + this.modelo);
        System.out.println("cor" + this.cor);
        System.out.println("rapidao: " + this.velocAtual + "KM/h");
        System.out.println("--------------------");
    }

}