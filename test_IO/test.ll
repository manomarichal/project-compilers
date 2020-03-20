declare i32 @printf(i8*, ...)
@istr = private constant [4 x i8] c"%d\0A\00"
@fstr = private constant [4 x i8] c"%f\0A\00"
define i32 @main() {
	start:
	; init %a as a
		%a = alloca float
	; %t1 = 1.3 + 0.0
		%t1 = fadd float 1.3, 0.0
	; assign %t1 to %a
		store float %t1, float* %a
	ret i32 0
}
