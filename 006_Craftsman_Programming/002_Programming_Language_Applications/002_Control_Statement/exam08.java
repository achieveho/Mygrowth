public class exam08 {
    public static void main(String[] args) {
        int input = 101110;
        int di = 1;
        int sum = 0;
        while (true) {
            if (input == 0) break;
            sum = sum + (input % 10) * di;
            di = di * 2;
            input = input / 10;
        }
        System.out.printf("%d", sum);
    }
}