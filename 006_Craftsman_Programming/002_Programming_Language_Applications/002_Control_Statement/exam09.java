public class exam09 {
    public static void main(String[] args) {
        int s, el = 0;
        for (int i = 6; i <= 30; i++) {
            s = 0;
            for (int j = 1; j <= i / 2; j++)
                if (i % j == 0)
                    s = s + j;
            if (s == i)
                el++;
        }
        System.out.printf("%d\n", el);
    }
}