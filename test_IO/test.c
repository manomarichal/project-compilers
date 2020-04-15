int main() {
    int x = 1;
    while (x < 10) {
        int result = x * 2;
        if ( x > 5) {
            result = result * x;
            }
        printf(result); //show the resultx = x + 1;
        x++;
    }
    return 0;
}