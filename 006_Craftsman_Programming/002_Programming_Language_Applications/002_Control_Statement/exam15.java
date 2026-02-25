public class exam15 {
    public static void main(String[] args) {
        int number = 1234;
        int div = 10, result = 0;

        while (number != 0) {
            result = result * div;
            result = result + number % 10;
            number = number / 10;
        }
        System.out.printf("%d", result);
    }
}