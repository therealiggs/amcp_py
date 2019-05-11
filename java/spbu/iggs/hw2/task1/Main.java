package spbu.iggs.hw2.task1;

import java.util.Scanner;

public class Main {
    public static void main(String[] args){

        Scanner s = new Scanner(System.in);
        Discount discount = new Discount();
        System.out.print("Введите хитрую скидку:");
        System.out.print( "Настоящая скидка: " + (discount.getRealDiscount(s.nextInt())));
    }
}

