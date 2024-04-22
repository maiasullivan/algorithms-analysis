class Swap {
    public static <T> void swap(T[] arr, int i, int j) {
        T temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
}

public class Bubble_sort {
    public static void main(String[] args) {
        Integer[] array = {5, 3, 8, 2, 1, 7, 4, 6};
        System.out.println("Original Array:");
        printArray(array);
        
        selsort(array);
        
        System.out.println("\nSorted Array:");
        printArray(array);
    }

    static <T extends Comparable<T>> void selsort(T[] A) {
        for (int i=0; i<A.length-1; i++) { // iterate using i 
            for (int j=1; j<A.length-i; j++) { // have a second iteration: responsible for swapping
                if (A[j-1].compareTo(A[j]) > 0) { // compares element with previous element
                    Swap.swap(A, j-1, j); // swaps if the left element is smaller
                }
            }
        }
    }
    
    static <T> void printArray(T[] array) {
        for (T item : array) {
            System.out.print(item + " ");
        }
        System.out.println();
    }
}
