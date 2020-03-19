declare i32 @printf(i8*, ...)
@str = private constant [4 x i8] c"%d\0A\00"
define i32 @main() {
	start:
	; init %a as a
		%a = alloca i32
	; load 10 in %t1
		%t1 = add i32 10, 0
	; assign %t1 to %a
		store i32 %t1, i32* %a
	; init %b as b
		%b = alloca i32
	; load 10 in %t2
		%t2 = add i32 10, 0
	; assign %t2 to %b
		store i32 %t2, i32* %b
	; init %c as c
		%c = alloca i32
	; load a in %t4
		%t4 = load i32, i32* %a
	; load b in %t5
		%t5 = load i32, i32* %b
	; %t3 = %t4 * %t5
		%t3 = mul i32 %t4, %t5
	; assign %t3 to %c
		store i32 %t3, i32* %c
	; load c in %t6
		%t6 = load i32, i32* %c
	; print %t6
		%t7 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8],[4 x i8]* @str,i32 0, i32 0),i32 %t6)
	; load c in %t8
		%t8 = load i32, i32* %c
	; print %t8
		%t9 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8],[4 x i8]* @str,i32 0, i32 0),i32 %t8)
	ret i32 0
}
