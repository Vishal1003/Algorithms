public class BitonicSort {
    static void kernel(int[] a, final int p, final int q) {
        final int d = 1 << (p-q);

        for(int i = 0; i < a.length; i++) {
            boolean up = ((i >> p) & 2) == 0;

            if ((i & d) == 0 && (a[i] > a[i | d]) == up) {
                int t = a[i];
                a[i] = a[i | d];
                a[i | d] = t;
            }
        }
    }

    static void bitonicSort(final int logn, int[] a) {
        assert a.length == 1 << logn;

        for(int i = 0; i < logn; i++) {
            for(int j = 0; j <= i; j++) {
                kernel(a, i, j);
            }
        }
    }

    public static void main(String[] args) {
        final int logn = 5, n = 1 << logn;

        int[] a0 = new int[n];
        for(int i = 0; i < n; i++) {
            a0[i] = (int)(Math.random() * 1000);
        }

        for(int k = 0; k < a0.length; k++) {
            System.out.print(a0[k] + " ");
        }
        System.out.println();

        bitonicSort(logn, a0);

        for(int k = 0; k < a0.length; k++) {
            System.out.print(a0[k] + " ");
        }
        System.out.println();
    }
}
