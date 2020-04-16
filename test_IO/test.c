
int main() {
    int c = 1;
    int *p = &c;
    int **p2 = &p;
    **p2 = 10;
    return c;
}