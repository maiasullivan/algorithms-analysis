import java.util.Arrays;

public class InsertionSort {
    public static <T extends Comparable<T>> void inssort(T[] A) {
        for (int i=1; i<A.length; i++) {
            for (int j=i; (j>0) && (A[j].compareTo(A[j-1]) < 0); j--) {
                swap(A, j-1, j);
            }
        }
    }

    private static <T> void swap(T[] array, int i, int j) {
        T temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }

    public static void main(String[] args) {
        Integer[] arr = {5, 2, 7, 1, 3};
        inssort(arr);
        System.out.println(Arrays.toString(arr));
    }
}