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
	; load a in %t3
		%t3 = load i32, i32* %a
	; %t2 = %t3 + 1
		%t2 = add i32 %t3, 1
	; assign %t2 to %a
		store i32 %t2, i32* %a
	; assign %t2 to %c
		store i32 %t2, i32* %c
	; init %e as e
		%e = alloca i32
	; load a in %t5
		%t5 = load i32, i32* %a
	; %t4 = %t5 - 1
		%t4 = sub i32 %t5, 1
	; assign %t4 to %a
		store i32 %t4, i32* %a
	; assign %t4 to %e
		store i32 %t4, i32* %e
	; load c in %t6
		%t6 = load i32, i32* %c
	; print %t6
		%t7 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8],[4 x i8]* @str,i32 0, i32 0),i32 %t6)
	; load e in %t8
		%t8 = load i32, i32* %e
	; print %t8
		%t9 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8],[4 x i8]* @str,i32 0, i32 0),i32 %t8)
	ret i32 0
}
