/*
 * Semantic errors & warnings
 * These tests are supposed to fail!
 */

// 3) typed semantics
const float my_var = 1 + 10.0 / 3;
my_var = 0.2;    // re-assigning to const var
