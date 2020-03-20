declare i32 @printf(i8*, ...)
@str = private constant [4 x i8] c"%d\0A\00"
define i32 @main() {
	start:
	; init %a as a
		%a = alloca i32
	; %t1 = 4 + 0
		%t1 = add i32 4, 0
	; %t2 = 3 + 0
		%t2 = add i32 3, 0
	; %t3 = %t1 > %t2
		%t3 = icmp sgt i32 %t1, %t2
	; %t4 = 1 + 0
		%t4 = add i32 1, 0
	; %t5 = 2 + 0
		%t5 = add i32 2, 0
	; %t6 = %t4 > %t5
		%t6 = icmp sgt i32 %t4, %t5
	; %t7 = %t3 and %t6
		%t7 = and i1 %t3, %t6
	; zero extent i1 %t7 to i32
		%t8 = zext i1 %t7 to i32
	; assign %t8 to %a
		store i32 %t8, i32* %a
	; init %b as b
		%b = alloca i32
	; %t9 = 4 + 0
		%t9 = add i32 4, 0
	; %t10 = 3 + 0
		%t10 = add i32 3, 0
	; %t11 = %t9 > %t10
		%t11 = icmp sgt i32 %t9, %t10
	; %t12 = 1 + 0
		%t12 = add i32 1, 0
	; %t13 = 2 + 0
		%t13 = add i32 2, 0
	; %t14 = %t12 > %t13
		%t14 = icmp sgt i32 %t12, %t13
	; %t15 = %t11 or %t14
		%t15 = or i1 %t11, %t14
	; zero extent i1 %t15 to i32
		%t16 = zext i1 %t15 to i32
	; assign %t16 to %b
		store i32 %t16, i32* %b
	; load a in %t17
		%t17 = load i32, i32* %a
	; print %t17
		%t18 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8],[4 x i8]* @str,i32 0, i32 0),i32 %t17)
	; load b in %t19
		%t19 = load i32, i32* %b
	; print %t19
		%t20 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8],[4 x i8]* @str,i32 0, i32 0),i32 %t19)
	ret i32 0
}
