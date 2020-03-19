declare i32 @printf(i8*, ...)
@str = private constant [4 x i8] c"%d\0A\00"
define i32 @main() {
	start:
	; init %x as x
		%x = alloca i32
	; load 5 in %t1
		%t1 = add i32 5, 0
	; load 13 in %t2
		%t2 = add i32 13, 0
	; load 10 in %t3
		%t3 = add i32 10, 0
	; %t4 = %t2 / %t3
		%t4 = udiv i32 %t2, %t3
	; load 29 in %t5
		%t5 = add i32 29, 0
	; load 10 in %t6
		%t6 = add i32 10, 0
	; %t7 = %t5 / %t6
		%t7 = udiv i32 %t5, %t6
	; %t8 = %t4 + %t7
		%t8 = add i32 %t4, %t7
	; %t9 = %t1 * %t8
		%t9 = mul i32 %t1, %t8
	; assign %t9 to %x
		store i32 %t9, i32* %x
	; init %y as y
		%y = alloca i32
	; load 100 in %t10
		%t10 = add i32 100, 0
	; load 89 in %t11
		%t11 = add i32 89, 0
	; %t12 = %t10 / %t11
		%t12 = udiv i32 %t10, %t11
	; load 10 in %t13
		%t13 = add i32 10, 0
	; %t14 = %t12 * %t13
		%t14 = mul i32 %t12, %t13
	; load 6 in %t15
		%t15 = add i32 6, 0
	; %t16 = %t14 - %t15
		%t16 = sub i32 %t14, %t15
	; assign %t16 to %y
		store i32 %t16, i32* %y
	; init %result as result
		%result = alloca i32
	; load x in %t18
		%t18 = load i32, i32* %x
	; load y in %t19
		%t19 = load i32, i32* %y
	; %t17 = %t18 + %t19
		%t17 = add i32 %t18, %t19
	; assign %t17 to %result
		store i32 %t17, i32* %result
	; load result in %t20
		%t20 = load i32, i32* %result
	; print %t20
		%t21 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8],[4 x i8]* @str,i32 0, i32 0),i32 %t20)
	ret i32 0
}
