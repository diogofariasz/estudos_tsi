import java.util.Scanner;

public class questao4 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Digite o salário do colaborador: ");
        double salario = scanner.nextDouble();
        double percentual = 0;
        if (salario <= 1000) {
            percentual = 20;
        } else if (salario <= 1500) {
            percentual = 15;
        } else if (salario <= 3000) {
            percentual = 10;
        } else {
            percentual = 5;
        }
        double aumento = salario * (percentual / 100);
        double novoSalario = salario + aumento;
        System.out.println("Salário antes do reajuste: R$ " + salario);
        System.out.println("Percentual aplicado: " + percentual + "%");
        System.out.println("Valor do aumento: R$ " + aumento);
        System.out.println("Novo salário: R$ " + novoSalario);
        scanner.close();
    }
}