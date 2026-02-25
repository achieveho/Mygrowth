public class exam08 {
    public static void main(String[] args) {
        int a = 5, b = 10, c = 15, d = 30;
        boolean result;
        result = a * 3 + b > d || c - b / a <= d && true;
        System.out.printf("%b\n", result);
    }
}