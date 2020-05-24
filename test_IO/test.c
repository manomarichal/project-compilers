#include <stdio.h>

int a;
float b;
int c;
// Should print the numbers 1 2 3

int main(){
	a = 5;
	b = a + 1.1;
	c = a + b + 'a';
	printf("%d", c);
	return 1;
}
