define i32 @main() {
start:
		%a = alloca i32
	; init %a as a
		%t1 = add i32 1, 0
	; load 1 in %t1
		store i32 %t1, i32* %a
	; assign %t1 to %a
		%b = alloca i32
	; init %b as b
		%t2 = add i32 2, 0
	; load 2 in %t2
		store i32 %t2, i32* %b
	; assign %t2 to %b
		%c = alloca i32
	; init %c as c
		%t4 = load i32*, %a
	; load a in %t4
		%t5 = load i32*, %b
	; load b in %t5
		%t3 = add i32 %t4, %t5
	; %t3 = %t4 + %t5
		store i32 %t3, i32* %c
	; assign %t3 to %c
}