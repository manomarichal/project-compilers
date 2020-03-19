declare i32 @printf(i8*, ...)
@str = private constant [4 x i8] c"%d\0A\00"
define i32 @main() {
	start:
	; init %a as a
		%a = alloca i32
	; %t1 = 5 + 0
		%t1 = add i32 5, 0
	; assign %t1 to %a
		store i32 %t1, i32* %a
	; init %c as c
		%c = alloca i32
	; assign  to %c
		store i32 , i32* %c
	; init %b as b
		%b = alloca i32
	; load a in %t3
		%t3 = load i32, i32* %a
	; load c in %t4
		%t4 = load i32, i32* %c
	; %t2 = %t3 + %t4
		%t2 = add i32 %t3, %t4
	; assign %t2 to %b
		store i32 %t2, i32* %b
	; init %c as c
		%c = alloca i32
	; %t5 = 5 + 0
		%t5 = add i32 5, 0
	; assign %t5 to %c
		store i32 %t5, i32* %c
	; init %d as d
		%d = alloca i32
	; load c in %t7
		%t7 = load i32, i32* %c
	; %t6 = %t7 + 1
		%t6 = add i32 %t7, 1
	; assign %t6 to %c
		store i32 %t6, i32* %c
	; assign %t6 to %d
		store i32 %t6, i32* %d
	; load b in %t8
		%t8 = load i32, i32* %b
	; print %t8
		%t9 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8],[4 x i8]* @str,i32 0, i32 0),i32 %t8)
	; load d in %t10
		%t10 = load i32, i32* %d
	; print %t10
		%t11 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8],[4 x i8]* @str,i32 0, i32 0),i32 %t10)
	ret i32 0
}
