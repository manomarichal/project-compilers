
#include <stdio.h>

int f(int a) {
	if (a<2) {
		return a;
	}
	else {
		return f(a-1) + f(a-2);
	}
	return 0;
}

// Recursive fibonnaci
int main(){
	int n;
    printf("Enter a number:");
	scanf("%d",&n);
	int i = 1;
	while(i++ <= n){
		printf("fib(%d)\t= %d;\n", i, f(i));
	}
	return 0;
}





//#include <stdio.h>
//
//// This should print the number 10 for each basic operation (int and float)
//int b;
//int ar[10];
//char c;
//float d;
//
//int main(){
//    for (int a = 0; a < 10; a++)
//    {
//        ar[a] = a;
//    }
//    for (int a = 0; a < 10; a++)
//    {
//        printf("this is a global variable: %d", ar[a]);
//    }
//    return 0;
//}
//



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
