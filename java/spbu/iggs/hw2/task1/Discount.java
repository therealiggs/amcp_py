package spbu.iggs.hw2.task1;

public class Discount {
    public int getRealDiscount(int discount){
        int sum = 0;
        while(discount > 9) {
            while (discount > 0) {
                sum += discount % 10;
                discount /= 10;
            }
            discount = sum;
            sum = 0;
        }
        return discount;

    }
}
