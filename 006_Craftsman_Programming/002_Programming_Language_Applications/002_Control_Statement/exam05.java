public class exam05 {
    public static void main(String[] args) {
        int v1 = 0;
        int v2 = 35;
        int v3 = 29;
        if ( (v1 > v2 ? v2 : v1) != 0 )
            v2 = v2 << 2;
        else
            v3 = v3 << 2;
        System.out.printf("%d", v2 + v3);
    }
}