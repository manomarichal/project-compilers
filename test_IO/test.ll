declare i32 @printf(i8*, ...)
@istr = private constant [4 x i8] c"%d\0A\00"
@fstr = private constant [4 x i8] c"%f\0A\00"
define i32 @main() {
	start:
	; init %x as x
		%x = alloca float
	; %t1 = 5.0 + 0.0
		%t1 = fadd float 5.0, 0.0
	; %t2 = 13.0 + 0.0
		%t2 = fadd float 13.0, 0.0
	; %t3 = 10.0 + 0.0
		%t3 = fadd float 10.0, 0.0
	; %t4 = %t2 / %t3
		%t4 = fdiv float %t2, %t3
	; %t5 = 29.0 + 0.0
		%t5 = fadd float 29.0, 0.0
	; %t6 = 10.0 + 0.0
		%t6 = fadd float 10.0, 0.0
	; %t7 = %t5 / %t6
		%t7 = fdiv float %t5, %t6
	; %t8 = %t4 + %t7
		%t8 = fadd float %t4, %t7
	; %t9 = %t1 * %t8
		%t9 = fmul float %t1, %t8
	; assign %t9 to %x
		store float %t9, float* %x
	; init %y as y
		%y = alloca float
	; %t10 = 100.0 + 0.0
		%t10 = fadd float 100.0, 0.0
	; %t11 = 89.0 + 0.0
		%t11 = fadd float 89.0, 0.0
	; %t12 = %t10 / %t11
		%t12 = fdiv float %t10, %t11
	; %t13 = 10.0 + 0.0
		%t13 = fadd float 10.0, 0.0
	; %t14 = %t12 * %t13
		%t14 = fmul float %t12, %t13
	; %t15 = 6.0 + 0.0
		%t15 = fadd float 6.0, 0.0
	; %t16 = %t14 - %t15
		%t16 = fsub float %t14, %t15
	; assign %t16 to %y
		store float %t16, float* %y
	; init %result as result
		%result = alloca float
	; load x in %t18
		%t18 = load float, float* %x
	; load y in %t19
		%t19 = load float, float* %y
	; %t17 = %t18 + %t19
		%t17 = fadd float %t18, %t19
	; assign %t17 to %result
		store float %t17, float* %result
	; load result in %t20
		%t20 = load float, float* %result
	; fp zero extent float %t20 to double
		%t21 = fpext float %t20 to double
	; print %t21
		%t22 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8],[4 x i8]* @fstr,i32 0, i32 0), double %t21)
	ret i32 0
}
