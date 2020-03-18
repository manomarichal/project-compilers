define i32 @main() {
	start:
	; init %x as x
		%x = alloca i32
	; load 6.0 in %t1
		%t1 = add none 6.0, 0
	; assign %t1 to %x
		store i32 %t1, i32* %x
	; init %y as y
		%y = alloca float
	; load 2 in %t2
		%t2 = add i32 2, 0
	; load x in %t4
		%t4 = load i32, i32* %x
	; %t3 = %t4 * %t2
		%t3 = mul i32 %t4, %t2
	; load 2.6666666666666665 in %t5
		%t5 = add none 2.6666666666666665, 0
	; load x in %t7
		%t7 = load i32, i32* %x
	; %t6 = %t5 + %t7
		%t6 = add none %t5, %t7
	; %t8 = %t3 / %t6
		%t8 = mod i32 %t3, %t6
	; load 16.0 in %t9
		%t9 = add none 16.0, 0
	; %t10 = %t8 + %t9
		%t10 = add i32 %t8, %t9
	; assign %t10 to %y
		store float %t10, float* %y
	; init %result as result
		%result = alloca float
	; load x in %t12
		%t12 = load i32, i32* %x
	; load y in %t13
		%t13 = load float, float* %y
	; %t11 = %t12 + %t13
		%t11 = add i32 %t12, %t13
	; assign %t11 to %result
		store float %t11, float* %result
	ret i32 0
}
