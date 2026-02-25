public class exam02 {
    public static void main(String[] args) {
        int i = 10, j = 10, k = 10;
        i /= j;
        j -= i;
        k %= j;
        System.out.printf("%d, %d, %d\n", i, j, k);
    }
}