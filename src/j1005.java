import java.util.Scanner;

public class j1005 {

    public static void main(String[] args) {

        Scanner ler = new Scanner(System.in);

        double A = ler.nextDouble();
        double B = ler.nextDouble();

        double media = ((A*3.5)+(B*7.5)) / 11;

        System.out.printf("MEDIA = %.5f\n", media);

    }

}
