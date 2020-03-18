define i32 @main() {
	start:
	; init %x as x
		%x = alloca float
	; load 95.0 in %t1
		%t1 = fadd float 95.0, 0.0
	; assign %t1 to %x
		store float %t1, float* %x
	; init %y as y
		%y = alloca float
	; load 2.5 in %t2
		%t2 = fadd float 2.5, 0.0
	; assign %t2 to %y
		store float %t2, float* %y
	; init %result as result
		%result = alloca float
	; load x in %t4
		%t4 = load float, float* %x
	; load y in %t5
		%t5 = load float, float* %y
	; %t3 = %t4 + %t5
		%t3 = fadd float %t4, %t5
	; assign %t3 to %result
		store float %t3, float* %result
	; init %a as a
		%a = alloca i32
	; load 7.0 in %t6
		%t6 = fadd float 7.0, 0.0
	; assign %t6 to %a
		store i32 %t6, i32* %a
	; init %b as b
		%b = alloca i32
	; load 20.0 in %t7
		%t7 = fadd float 20.0, 0.0
	; assign %t7 to %b
		store i32 %t7, i32* %b
	ret i32 0
}
