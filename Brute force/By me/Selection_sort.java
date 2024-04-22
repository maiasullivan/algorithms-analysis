class Swap {
    public static <T> void swap(T[] arr, int i, int j) {
        T temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
}

public class Selection_sort {
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
            int bigindex = 0; // set difference between i and largest element to 0
            for (int j=1; j<A.length-i; j++) { // have a second iteration to find the largest element in the unsorted array
                if (A[j].compareTo(A[bigindex]) > 0) { // select the largest element
                    bigindex = j; // replace this as the 'bigindex'
                }
            }
            Swap.swap(A, bigindex, A.length-i-1); // put bigindex at the end of unsorted array/start of the sorted array
        }
    }
    
    static <T> void printArray(T[] array) {
        for (T item : array) {
            System.out.print(item + " ");
        }
        System.out.println();
    }
}
