public class exam09 {
    public static void main(String[] args) {
        int m = 4620;
        int a = m / 1000;
        int b = (m % 1000) / 500;
        int c = (m % 500) / 100;
        int d = (m % 100) / 10;
        System.out.printf("1000원의 개수 : %d\n", a);
        System.out.printf("500원의 개수 : %d\n", b);
        System.out.printf("100원의 개수 : %d\n", c);
        System.out.printf("10원의 개수 : %d\n", d);
    }
}