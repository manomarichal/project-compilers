#include <stdio.h>

int a[2];
float b[2];
int c;
float d;
// Should print the numbers 1 2 3

int main(){
	a[0] = 1;
	a[1] = 2;
	b[0] = 1;
	b[1] = 2;
	c = 1;
	d = 2;
	printf("%d", a[0]);
	printf("%d", a[1]);
	printf("%f", b[0]);
	printf("%f", b[1]);
	printf("%d", c);
	printf("%f", d);
	return 1;
}
