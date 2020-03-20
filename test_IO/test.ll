declare i32 @printf(i8*, ...)
@istr = private constant [4 x i8] c"%d\0A\00"
@fstr = private constant [4 x i8] c"%f\0A\00"
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
	; %t15 = %t13 <= %t14
		%t15 = icmp sle i32 %t13, %t14
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
	; init %g as g
		%g = alloca float
	; %t25 = 1.0 + 0.0
		%t25 = fadd float 1.0, 0.0
	; %t26 = 2.0 + 0.0
		%t26 = fadd float 2.0, 0.0
	; %t27 = %t25 > %t26
		%t27 = fcmp ogt float %t25, %t26
	; unsigned int i1 %t27 to float
		%t28 = uitofp i1 %t27 to float
	; assign %t28 to %g
		store float %t28, float* %g
	; init %h as h
		%h = alloca float
	; %t29 = 1.0 + 0.0
		%t29 = fadd float 1.0, 0.0
	; %t30 = 2.0 + 0.0
		%t30 = fadd float 2.0, 0.0
	; %t31 = %t29 < %t30
		%t31 = fcmp olt float %t29, %t30
	; unsigned int i1 %t31 to float
		%t32 = uitofp i1 %t31 to float
	; assign %t32 to %h
		store float %t32, float* %h
	; init %i as i
		%i = alloca float
	; %t33 = 1.0 + 0.0
		%t33 = fadd float 1.0, 0.0
	; %t34 = 2.0 + 0.0
		%t34 = fadd float 2.0, 0.0
	; %t35 = %t33 >= %t34
		%t35 = fcmp oge float %t33, %t34
	; unsigned int i1 %t35 to float
		%t36 = uitofp i1 %t35 to float
	; assign %t36 to %i
		store float %t36, float* %i
	; init %j as j
		%j = alloca float
	; %t37 = 1.0 + 0.0
		%t37 = fadd float 1.0, 0.0
	; %t38 = 2.0 + 0.0
		%t38 = fadd float 2.0, 0.0
	; %t39 = %t37 <= %t38
		%t39 = fcmp ole float %t37, %t38
	; unsigned int i1 %t39 to float
		%t40 = uitofp i1 %t39 to float
	; assign %t40 to %j
		store float %t40, float* %j
	; init %k as k
		%k = alloca float
	; %t41 = 1.0 + 0.0
		%t41 = fadd float 1.0, 0.0
	; %t42 = 2.0 + 0.0
		%t42 = fadd float 2.0, 0.0
	; %t43 = %t41 == %t42
		%t43 = fcmp oeq float %t41, %t42
	; unsigned int i1 %t43 to float
		%t44 = uitofp i1 %t43 to float
	; assign %t44 to %k
		store float %t44, float* %k
	; init %l as l
		%l = alloca float
	; %t45 = 1.0 + 0.0
		%t45 = fadd float 1.0, 0.0
	; %t46 = 2.0 + 0.0
		%t46 = fadd float 2.0, 0.0
	; %t47 = %t45 != %t46
		%t47 = fcmp one float %t45, %t46
	; unsigned int i1 %t47 to float
		%t48 = uitofp i1 %t47 to float
	; assign %t48 to %l
		store float %t48, float* %l
	; load a in %t49
		%t49 = load i32, i32* %a
	; print %t49
		%t50 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8],[4 x i8]* @istr,i32 0, i32 0),i32 %t49)
	; load b in %t51
		%t51 = load i32, i32* %b
	; print %t51
		%t52 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8],[4 x i8]* @istr,i32 0, i32 0),i32 %t51)
	; load c in %t53
		%t53 = load i32, i32* %c
	; print %t53
		%t54 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8],[4 x i8]* @istr,i32 0, i32 0),i32 %t53)
	; load d in %t55
		%t55 = load i32, i32* %d
	; print %t55
		%t56 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8],[4 x i8]* @istr,i32 0, i32 0),i32 %t55)
	; load e in %t57
		%t57 = load i32, i32* %e
	; print %t57
		%t58 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8],[4 x i8]* @istr,i32 0, i32 0),i32 %t57)
	; load f in %t59
		%t59 = load i32, i32* %f
	; print %t59
		%t60 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8],[4 x i8]* @istr,i32 0, i32 0),i32 %t59)
	; load g in %t61
		%t61 = load float, float* %g
	; fp zero extent float %t61 to double
		%t62 = fpext float %t61 to double
	; print %t62
		%t63 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8],[4 x i8]* @fstr,i32 0, i32 0), double %t62)
	; load h in %t64
		%t64 = load float, float* %h
	; fp zero extent float %t64 to double
		%t65 = fpext float %t64 to double
	; print %t65
		%t66 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8],[4 x i8]* @fstr,i32 0, i32 0), double %t65)
	; load i in %t67
		%t67 = load float, float* %i
	; fp zero extent float %t67 to double
		%t68 = fpext float %t67 to double
	; print %t68
		%t69 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8],[4 x i8]* @fstr,i32 0, i32 0), double %t68)
	; load j in %t70
		%t70 = load float, float* %j
	; fp zero extent float %t70 to double
		%t71 = fpext float %t70 to double
	; print %t71
		%t72 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8],[4 x i8]* @fstr,i32 0, i32 0), double %t71)
	; load k in %t73
		%t73 = load float, float* %k
	; fp zero extent float %t73 to double
		%t74 = fpext float %t73 to double
	; print %t74
		%t75 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8],[4 x i8]* @fstr,i32 0, i32 0), double %t74)
	; load l in %t76
		%t76 = load float, float* %l
	; fp zero extent float %t76 to double
		%t77 = fpext float %t76 to double
	; print %t77
		%t78 = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8],[4 x i8]* @fstr,i32 0, i32 0), double %t77)
	ret i32 0
}
