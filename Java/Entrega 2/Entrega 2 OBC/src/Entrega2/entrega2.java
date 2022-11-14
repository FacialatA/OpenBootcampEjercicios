package Entrega2;

import java.util.Scanner;

public class entrega2 {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        System.out.println("Introduce el precio: ");
        int numero = scanner.nextInt();
        double precioFinal = numero + numero * 0.21;
        System.out.println("El precio final es: " + precioFinal);

    }
}
