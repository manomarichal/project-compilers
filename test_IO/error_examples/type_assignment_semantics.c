/*
 * Semantic errors & warnings
 * These tests are supposed to fail!
 */

// 2) type assignment errors
int a = 0.3;    // (warning) implicit conversion
a = *10;    // de-referencing non-ptr
char b = 'a';
a = b;
