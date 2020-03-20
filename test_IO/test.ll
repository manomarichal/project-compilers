declare i32 @printf(i8*, ...)
@str = private constant [4 x i8] c"%d\0A\00"
define i32 @main() {
	start:
	; init %a as a
		%a = alloca i32
	; %t1 = 1 + 0
		%t1 = add i32 1, 0
	; %t2 = 2 + 0
		%t2 = add i32 2, 0
	; %t3 = %t1 > %t2
		%t3 = icmp sgt i32 %t1, %t2
	; zero extent i1 %t3 to i32
		%t4 = zext i1 %t3 to i32
	; assign %t4 to %a
		store i32 %t4, i32* %a
	; init %b as b
		%b = alloca i32
	; %t5 = 1 + 0
		%t5 = add i32 1, 0
	; %t6 = 2 + 0
		%t6 = add i32 2, 0
	; %t7 = %t5 < %t6
		%t7 = icmp slt i32 %t5, %t6
	; zero extent i1 %t7 to i32
		%t8 = zext i1 %t7 to i32
	; assign %t8 to %b
		store i32 %t8, i32* %b
	; init %c as c
		%c = alloca i32
	; %t9 = 1 + 0
		%t9 = add i32 1, 0
	; %t10 = 2 + 0
		%t10 = add i32 2, 0
	; %t11 = %t9 >= %t10
		%t11 = icmp sge i32 %t9, %t10
	; zero extent i1 %t11 to i32
		%t12 = zext i1 %t11 to i32
	; assign %t12 to %c
		store i32 %t12, i32* %c
	; init %d as d
		%d = alloca i32
	; %t13 = 1 + 0
		%t13 = add i32 1, 0
	; %t14 = 2 + 0
		%t14 = add i32 2, 0
	; %t15 = %t13 >= %t14
		%t15 = icmp sge i32 %t13, %t14
	; zero extent i1 %t15 to i32
		%t16 = zext i1 %t15 to i32
	; assign %t16 to %d
		store i32 %t16, i32* %d
	; init %e as e
		%e = alloca i32
	; %t17 = 1 + 0
		%t17 = add i32 1, 0
	; %t18 = 2 + 0
		%t18 = add i32 2, 0
	; %t19 = %t17 == %t18
		%t19 = icmp eq i32 %t17, %t18
	; zero extent i1 %t19 to i32
		%t20 = zext i1 %t19 to i32
	; assign %t20 to %e
		store i32 %t20, i32* %e
	; init %f as f
		%f = alloca i32
	; %t21 = 1 + 0
		%t21 = add i32 1, 0
	; %t22 = 2 + 0
		%t22 = add i32 2, 0
	; %t23 = %t21 != %t22
		%t23 = icmp ne i32 %t21, %t22
	; zero extent i1 %t23 to i32
		%t24 = zext i1 %t23 to i32
	; assign %t24 to %f
		store i32 %t24, i32* %f
	; load a in %t25
		%t25 = load i32, i32* %a
	; print %t25
		%t26 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8],[4 x i8]* @str,i32 0, i32 0),i32 %t25)
	; load b in %t27
		%t27 = load i32, i32* %b
	; print %t27
		%t28 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8],[4 x i8]* @str,i32 0, i32 0),i32 %t27)
	; load c in %t29
		%t29 = load i32, i32* %c
	; print %t29
		%t30 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8],[4 x i8]* @str,i32 0, i32 0),i32 %t29)
	; load d in %t31
		%t31 = load i32, i32* %d
	; print %t31
		%t32 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8],[4 x i8]* @str,i32 0, i32 0),i32 %t31)
	; load e in %t33
		%t33 = load i32, i32* %e
	; print %t33
		%t34 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8],[4 x i8]* @str,i32 0, i32 0),i32 %t33)
	; load f in %t35
		%t35 = load i32, i32* %f
	; print %t35
		%t36 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8],[4 x i8]* @str,i32 0, i32 0),i32 %t35)
	ret i32 0
}
