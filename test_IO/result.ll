define i32 @main() {
	start:
	; init %a as a
		%a = alloca i32
	; load True in %t1
		%t1 = add none True, 0
	; assign %t1 to %a
		store i32 %t1, i32* %a
	; init %x as x
		%x = alloca i32
	; load 6.0 in %t2
		%t2 = add none 6.0, 0
	; assign %t2 to %x
		store i32 %t2, i32* %x
	; init %y as y
		%y = alloca float
	; load 2 in %t3
		%t3 = add i32 2, 0
	; load x in %t5
		%t5 = load i32, i32* %x
	; %t4 = %t5 * %t3
		%t4 = mul i32 %t5, %t3
	; load 2.6666666666666665 in %t6
		%t6 = add none 2.6666666666666665, 0
	; load x in %t8
		%t8 = load i32, i32* %x
	; %t7 = %t6 + %t8
		%t7 = add none %t6, %t8
	; %t9 = %t4 / %t7
		%t9 = mod i32 %t4, %t7
	; load 16.0 in %t10
		%t10 = add none 16.0, 0
	; %t11 = %t9 + %t10
		%t11 = add i32 %t9, %t10
	; assign %t11 to %y
		store float %t11, float* %y
	; init %result as result
		%result = alloca float
	; load x in %t13
		%t13 = load i32, i32* %x
	; load y in %t14
		%t14 = load float, float* %y
	; %t12 = %t13 + %t14
		%t12 = add i32 %t13, %t14
	; assign %t12 to %result
		store float %t12, float* %result
	ret i32 0
}
