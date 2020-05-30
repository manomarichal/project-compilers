#include <stdio.h>

int main(){
    int t1 = 10;
    int t2 = 20;
    int t3 = 30;
	int * a[3];
	a[0] = &t1;
	a[1] = &t2;
	a[2] = &t3;
	a[0] = a[2];
	printf("%d", *a[0] + *a[1] + *a[2]);
	return 1;
}

// expected 80

