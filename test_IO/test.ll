declare i32 @printf(i8*, ...)
@istr = private constant [4 x i8] c"%d\0A\00"
@fstr = private constant [4 x i8] c"%f\0A\00"
define i32 @main() {
	start:
	; init %c as c
		%c = alloca i32
	; %t1 = 1.5 + 0.0
		%t1 = fadd float 1.5, 0.0
	; float float %t1 to signed i32
		%t2 = fptosi float %t1 to i32
	; assign %t2 to %c
		store i32 %t2, i32* %c
	; init %d as d
		%d = alloca i32
	; %t3 = 4 + 0
		%t3 = add i32 4, 0
	; %t4 = 3 + 0
		%t4 = add i32 3, 0
	; %t5 = %t3 > %t4
		%t5 = icmp sgt i32 %t3, %t4
	; zero extent i1 %t5 to i32
		%t6 = zext i1 %t5 to i32
	; assign %t6 to %d
		store i32 %t6, i32* %d
	; init %e as e
		%e = alloca float
	; %t7 = 4 + 0
		%t7 = add i32 4, 0
	; %t8 = 3 + 0
		%t8 = add i32 3, 0
	; %t9 = %t7 > %t8
		%t9 = icmp sgt i32 %t7, %t8
	; unsigned int i1 %t9 to float
		%t10 = uitofp i1 %t9 to float
	; assign %t10 to %e
		store float %t10, float* %e
	; init %f as f
		%f = alloca float
	; %t11 = 10 + 0
		%t11 = add i32 10, 0
	; signed int i32 %t11 to float
		%t12 = sitofp i32 %t11 to float
	; assign %t12 to %f
		store float %t12, float* %f
	; load c in %t13
		%t13 = load i32, i32* %c
	; print %t13
		%t14 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8],[4 x i8]* @istr,i32 0, i32 0),i32 %t13)
	; load d in %t15
		%t15 = load i32, i32* %d
	; print %t15
		%t16 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8],[4 x i8]* @istr,i32 0, i32 0),i32 %t15)
	; load e in %t17
		%t17 = load float, float* %e
	; fp zero extent float %t17 to double
		%t18 = fpext float %t17 to double
	; print %t18
		%t19 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8],[4 x i8]* @fstr,i32 0, i32 0), double %t18)
	; load f in %t20
		%t20 = load float, float* %f
	; fp zero extent float %t20 to double
		%t21 = fpext float %t20 to double
	; print %t21
		%t22 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8],[4 x i8]* @fstr,i32 0, i32 0), double %t21)
	ret i32 0
}
