declare i32 @printf(i8*, ...)
@istr = private constant [4 x i8] c"%d\0A\00"
@fstr = private constant [4 x i8] c"%f\0A\00"
define i32 @main() {
	start:
	; init %a as a
		%a = alloca i32
	; %t1 = 1 + 0
		%t1 = add i32 1, 0
	; assign %t1 to %a
		store i32 %t1, i32* %a
	; init %b as b
		%b = alloca i32
	; %t2 = 5 + 0
		%t2 = add i32 5, 0
	; assign %t2 to %b
		store i32 %t2, i32* %b
	; init %p as p
		%p = alloca i32*
	; get adress of %a
		%t3 = getelementptr i32, i32* %a
	; assign %t3 to %p
		store i32* %t3, i32** %p
	; load %p in %t4
		%t4 = load i32*, i32** %p
	; load %b in %t5
		%t5 = load i32, i32* %b
	; assign %t5 to %t4
		store i32 %t5, i32* %t4
	; init %c as c
		%c = alloca i32
	; load %p in %t6
		%t6 = load i32*, i32** %p
	; load %t6 in %t7
		%t7 = load i32, i32* %t6
	; assign %t7 to %c
		store i32 %t7, i32* %c
	; load %c in %t8
		%t8 = load i32, i32* %c
	; print %t8
		%t9 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8],[4 x i8]* @istr,i32 0, i32 0),i32 %t8)
	ret i32 0
}
