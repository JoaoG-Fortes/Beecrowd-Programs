import java.util.Scanner;

public class j1002 {

    public static void main(String[] args) {

        Scanner ler = new Scanner(System.in);
        double raio = 0;
        double area = 0;

        System.out.println();
        raio = ler.nextDouble();

        area = 3.14159 * Math.pow(raio, 2);

        System.out.printf("A=%.4f", area);
        System.out.println();

    }

}
