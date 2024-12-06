import java.util.Scanner;
public class questao1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int pares = 0, impares = 0;
        for (int i = 0; i < 20; i++) {
            System.out.print("Digite um número: ");
            int numero = scanner.nextInt();
            if (numero >= 0) {
                if (numero % 2 == 0) {
                    pares++;
                } else {
                    impares++;
                }
            }
        }
        System.out.println("Quantidade de pares: " + pares);
        System.out.println("Quantidade de ímpares: " + impares);
        scanner.close();
    }
}
