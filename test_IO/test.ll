declare i32 @printf(i8*, ...)
@istr = private constant [4 x i8] c"%d\0A\00"
@fstr = private constant [4 x i8] c"%f\0A\00"
define i32 @main() {
	start:
	; init %a as a
		%a = alloca i32
	; %t1 = 5 + 0
		%t1 = add i32 5, 0
	; assign %t1 to %a
		store i32 %t1, i32* %a
	; init %b as b
		%b = alloca float
	; %t2 = 5.0 + 0.0
		%t2 = fadd float 5.0, 0.0
	; assign %t2 to %b
		store float %t2, float* %b
	; load a in %t3
		%t3 = load i32, i32* %a
	; print %t3
		%t4 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8],[4 x i8]* @istr,i32 0, i32 0),i32 %t3)
	; load b in %t5
		%t5 = load float, float* %b
	; fp zero extent float %t5 to double
		%t6 = fpext float %t5 to double
	; print %t6
		%t7 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8],[4 x i8]* @fstr,i32 0, i32 0), double %t6)
	ret i32 0
}
