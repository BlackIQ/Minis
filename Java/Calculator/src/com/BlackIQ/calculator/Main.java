package com.BlackIQ.calculator;

/*
    +--------------------------------------------------+
    | Name         :      Java Calculator              |
    | Version      :      0.0.1                        |
    | Date         :      Dec 24 2020                  |
    | Programmer   :      Amirhossein Mohammadi        |
    | Github       :      https://github.com/BlackIQ   |
    | Language     :     Java                          |
    | Last Update  :     Dec 24 2020                   |
    +--------------------------------------------------+
 */

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        System.out.println("Welcome to This Java Calculator !\n\n");

        Scanner input = new Scanner(System.in);

        System.out.print("Enter Number 1 pls : ");
        int number1 = input.nextInt();

        System.out.println("I Got number 1 !");

        System.out.print("\nEnter Number 2 pls : ");
        int number2 = input.nextInt();

        System.out.println("I Got number 2 !");
        System.out.println("\nLets calculate !\n");

        int plus = number1 + number2;
        int min = number1 - number2;
        int mul = number1 * number2;
        int div = number1 / number2;

        System.out.println("Number1 + Number2 = " + plus + " => " + number1 + " + " + number2 + " = " + plus + "\n");

        System.out.println("Number1 - Number2 = " + min + " => " + number1 + " - " + number2 + " = " + min + "\n");

        System.out.println("Number1 * Number2 = " + mul + " => " + number1 + " * " + number2 + " = " + mul + "\n");

        System.out.println("Number1 / Number2 = " + div + " => " + number1 + " / " + number2 + " = " + div + "\n");
    }
}
