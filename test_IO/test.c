#include <stdio.h>

// This should print 1 and 0 alternating
int main(){
        printf("%d; ", 1 && 2);
        printf("%d; ", 0 && 2);
        printf("%d; ", 1 || 2);
        printf("%d; ", 0 || 0);
        return 1;
}
