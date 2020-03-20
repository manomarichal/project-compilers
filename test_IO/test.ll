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
	; init %p1 as p1
		%p1 = alloca i32*
	; get adress of %a
		%t3 = getelementptr i32, i32* %a
	; assign %t3 to %p1
		store i32* %t3, i32** %p1
	; init %p2 as p2
		%p2 = alloca i32**
	; get adress of %p1
		%t4 = getelementptr i32*, i32** %p1
	; assign %t4 to %p2
		store i32** %t4, i32*** %p2
	; init %p3 as p3
		%p3 = alloca i32***
	; get adress of %p2
		%t5 = getelementptr i32**, i32*** %p2
	; assign %t5 to %p3
		store i32*** %t5, i32**** %p3
	; load %p3 in %t6
		%t6 = load i32***, i32**** %p3
	; load %t6 in %t7
		%t7 = load i32**, i32*** %t6
	; load %t7 in %t8
		%t8 = load i32*, i32** %t7
	; load %b in %t9
		%t9 = load i32, i32* %b
	; assign %t9 to %t8
		store i32 %t9, i32* %t8
	; load %a in %t10
		%t10 = load i32, i32* %a
	; print %t10
		%t11 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8],[4 x i8]* @istr,i32 0, i32 0),i32 %t10)
	; load %b in %t12
		%t12 = load i32, i32* %b
	; print %t12
		%t13 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8],[4 x i8]* @istr,i32 0, i32 0),i32 %t12)
	ret i32 0
}
