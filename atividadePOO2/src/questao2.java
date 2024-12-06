//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
import java.util.Scanner;
public class questao2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Digite a primeira nota: ");
        double nota1 = scanner.nextDouble();
        System.out.print("Digite a segunda nota: ");
        double nota2 = scanner.nextDouble();
        double media = (nota1 + nota2) / 2;
        System.out.println("Média: " + media);
        if (media >= 7) {
            System.out.println("Mensagem: Aprovado");
        } else if (media >= 5) {
            System.out.println("Mensagem: Recuperação");
        } else {
            System.out.println("Mensagem: Reprovado");
        }
        if (media == 10) {
            System.out.println("Mensagem: Aprovado com Distinção");
        }
        scanner.close();
    }
}