import java.util.Scanner;
public class questao5 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.print("Digite o primeiro lado do triângulo: ");
            double lado1 = scanner.nextDouble();
            System.out.print("Digite o segundo lado do triângulo: ");
            double lado2 = scanner.nextDouble();
            System.out.print("Digite o terceiro lado do triângulo: ");
            double lado3 = scanner.nextDouble();
            if (lado1 + lado2 > lado3 && lado1 + lado3 > lado2 && lado2 + lado3 > lado1) {
                System.out.println("Os valores formam um triângulo.");
                if (lado1 == lado2 && lado2 == lado3) {
                    System.out.println("O triângulo é equilátero.");
                } else if (lado1 == lado2 || lado1 == lado3 || lado2 == lado3) {
                    System.out.println("O triângulo é isósceles.");
                } else {
                    System.out.println("O triângulo é escaleno.");
                }
            } else {
                System.out.println("Os valores não formam um triângulo.");
            }
            System.out.print("Deseja realizar outro teste? (s/n): ");
            char resposta = scanner.next().toLowerCase().charAt(0);
            if (resposta != 's') {
                break;
            }
        }
        scanner.close();
    }
}
