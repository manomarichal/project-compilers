/*
 * Semantic errors & warnings
 * These tests are supposed to fail!
 */

// 1) un-typed semantics
int foo;
foo=foo;    // (warning) usage of uninitialised variable
int a = &10;    // address of r-val
int a = 5;    // re-declaration
b = 'a';    // undeclared
