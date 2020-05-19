int main() {
    int t1 = 0;
    int t2 = 1;
    int nextTerm = 0;
    int n = 1000;

    // displays the first two terms which is always 0 and 1
    nextTerm = t1 + t2;

    while (nextTerm <= n) {
        printf(nextTerm);
        t1 = t2;
        t2 = nextTerm;
        nextTerm = t1 + t2;
    }

    return 0;
}