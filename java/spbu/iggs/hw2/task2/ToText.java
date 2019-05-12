package spbu.iggs.hw2.task2;

public class ToText {
    int number;

    public ToText(int num){
        this.number = num;
    }

    public String toText() {
        String text = "";
        if (number == 1000){
            text = "тысяча";
        }
        else {
            switch (number / 100) {
                case 1:
                    text += "сто";
                    break;
                case 2:
                    text += "двести";
                    break;
                case 3:
                    text += "триста";
                    break;
                case 4:
                    text += "четыреста";
                    break;
                case 5:
                    text += "пятьсот";
                    break;
                case 6:
                    text += "шестьсот";
                    break;
                case 7:
                    text += "семьсот";
                    break;
                case 8:
                    text += "восемьсот";
                    break;
                case 9:
                    text += "девятьсот";
                    break;
            }

            switch ((number % 100)/10) {
                case 2:
                    text += "двадцать";
                    break;
                case 3:
                    text += "тридцать";
                    break;
                case 4:
                    text += "сорок";
                    break;
                case 5:
                    text += "пятьдесят";
                    break;
                case 6:
                    text += "шестьдесят";
                    break;
                case 7:
                    text += "семьдесят";
                    break;
                case 8:
                    text += "восемьдесят";
                    break;
                case 9:
                    text += "девяносто";
                    break;
            }

            switch (number % 100) {
                case 10:
                    text += "десять";
                    break;
                case 11:
                    text += "одиннадцать";
                    break;
                case 12:
                    text += "двенадцать";
                    break;
                case 13:
                    text += "тринадцать";
                    break;
                case 14:
                    text += "четырнадцать";
                    break;
                case 15:
                    text += "пятнадцать";
                    break;
                case 16:
                    text += "шестнадцать";
                    break;
                case 17:
                    text += "семнадцать";
                    break;
                case 18:
                    text += "восемнадцать";
                    break;
                case 19:
                    text += "девятнадцать";
                    break;
                default:
                    switch (number % 10){
                        case 1:
                            text += "один";
                            break;
                        case 2:
                            text += "два";
                            break;
                        case 3:
                            text += "три";
                            break;
                        case 4:
                            text += "четыре";
                            break;
                        case 5:
                            text += "пять";
                            break;
                        case 6:
                            text += "шесть";
                            break;
                        case 7:
                            text += "семь";
                            break;
                        case 8:
                            text += "восемь";
                            break;
                        case 9:
                            text += "девять";
                            break;
                    }
                break;

            }
    }
        return text;
}
}

