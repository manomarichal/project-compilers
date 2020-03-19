declare i32 @printf(i8*, ...)
@str = private constant [4 x i8] c"%d\0A\00"
define i32 @main() {
	start:
	; init %a as a
		%a = alloca float
	; %t1 = 1.0 + 0.0
		%t1 = fadd float 2.0, 0.0
	; assign %t1 to %a
		store float %t1, float* %a
	    %conv1 = fpext float %t1 to double
        %cmp = fcmp oeq float %t1, 2.000000e+00
        %conv2 = zext i1 %cmp to i32
        %call = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8],[4 x i8]* @str,i32 0, i32 0), i32 %conv2)

	ret i32 0
}
