#include <stdio.h>

// This should print the number 10 for each basic operation (int and float)
int main(){
        printf("%d; ", 5+5);
        printf("%f; ", 4.5+5.5);
        printf("%d; ", 15-5);
        printf("%f; ", 10.5-0.5);
        printf("%d; ", 2*5);
        printf("%f; ", 20.0*0.5);
        printf("%d; ", 20/2);
        printf("%f; ", 5.0/0.5);
        return 1;
}




//
//
//void swap(int *xp, int *yp)
//{
//    int temp = *xp;
//    *xp = *yp;
//    *yp = temp;
//}
//
//void bubbleSort(int arr[10])
//{
//    for (int i = 0; i < 5; i = i + 1)
//    {
//       for (int j = 0; j < 5-i-1; j = j + 1)
//       {
//           if (1 > 3)
//           {
//              swap(&arr[j], &arr[j+1]);
//           }
//       }
//   }
//}
//
///* Function to print an array */
//int printArray(int arr[10])
//{
//    int i;
//    for (i=0; i < 10; i = i + 1) {
//    printf(arr[i]);
//    }
//    return 0;
//}
//
//int main()
//{
//    int arr[10];
//    arr[0] = 10;
//    arr[1] = 12;
//    arr[2] = 8;
//    arr[3] = 6;
//    arr[4] = 3;
//    arr[5] = -4;
//    arr[6] = 0;
//    arr[7] = 11;
//    arr[8] = 13;
//    arr[9] = 18;
//    bubbleSort(arr);
//    printArray(arr);
//    return 0;
//}
