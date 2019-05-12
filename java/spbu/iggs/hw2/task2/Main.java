package spbu.iggs.hw2.task2; // Это задание залито на 5 часов позже дедлайна, но не могли бы Вы проверить его не оценивая?
// Если здесь есть баги я бы очень хотел знать, я хочу лучше научиться джаве и ооп

import java.util.Scanner;

public class Main {
    public static void main(String[] Args) {
        int sum = 0;
        String text = "";
        for (int i = 1; i <= 1000; i++) {
            ToText number = new ToText(i);
            text = number.toText();
            sum += text.length();
        }
        System.out.println(sum);
        Scanner s = new Scanner(System.in);
        while(true) {
            ToText exmpl = new ToText(s.nextInt());
            System.out.println(exmpl.toText());
        }
    }
}
