#  Đây là file hướng dẫn các fuction cơ bản
# Strings:
# -len: để đếm kí tự
# -.replace: để thay  thế kí tự
# -.index: tìm kiêm thứ tự của chữ cái
# -[]: trích xuất chữ cái [::-1] là đảo ngược chữ 
# -'\n': xuống dòng
# """ """ : cũng xuống dòng nhưng dài hơn
# -" ".join() : hàm để kết hợp str
# -.split(): ham tách từng giá trị của str 

# numbers:
# -**: dấu mũ
# -%: thực hiện phép chia và trả về số dư
# -pow: hàm thực hiện mũ
# -max: hàm tìm giá trị lớn nhất  
# -abs: hàm giá trị tuyệt đối
# -min :hàm tìm giá trị nhỏ nhất
# -round: hàm làm tròn số
# -int: chuyển str thành số NGUYÊN
# -float: chuyển Str thành số thực 
# from math import *
# # -floor: hàm tăng giá trị dù có như nào
# # -cecil: hàm giảm giá trị dù có như nào
# # -sqrt: hàm căn
# -copysign: hàm lấy giá trị số thứ nhất và dấu số thứ hai 
# -erf: trả về hàm lỗi của một số 

# lists: []
# -.extend: dùng để kết hợp hai list lại với nhau
# -.append: dùng để thêm giá trị vào list
# -.insert: dùng để thêm giá trị vào bất cứ chỗ nào trong list (vị trí thêm, giá trị thêm)
# -.remove: dùng để loại bỏ giá trị ra khỏi list
# -.clear: dùng để dọn sạch list 
# -.pop: loại bỏ giá trị cuối của list
# -.sort: sắp xếp các giá trị trong list từ thấp đến cao
# -.converse: sắp xếp các giá trị từ cao đến thấp  
# -copy: sao chép giá trị list này sang list khác
# -.count: hàm đếm kí tự

# number_grid = [
# [1,2,3],
# [4,5,6],
# [7,8,9],
# [0]
# ]
# print(number_grid[0][2])(cột đầu tiên là thứ tự list,cột thứ hai là thứ tự của giá trị)
# result : 3 


# tupple: ()
# - tupple không thể thay đổi giá trị được
 
# -dictionnaries:{}
# -.get: dùng để tìm kiếm key (key cần tìm, trường hợp nếu không  tìm thấy key )

# def comparision(num1,num2,num3,num4):
# 	hayla = { (num1,num2,num3,num4):[num1,num2,num3,num4]}
# 	a = hayla[(num1,num2,num3,num4)] 
# 	a.sort()
# 	print(a)
# comparision(9,8,7,6)

# def raise_to_power(base_num, pow_num):
# 	return base_num** pow_num
# 	num = {(base_num**pow_num): a }
# 	print(num[a]) 

# print(raise_to_power(2,3))

# result : 8 

# # while loop: vòng tuần hoàn

# a +=1 tương đương a = a + 1 
# a = 1
# while  a <= 200:
# 	print(a)
# 	a += 2**2 

# print("done")

# keyworld = "haiya"
# player = input("""please guess the world Uncle Roger always say in his video, you have 3 chance
# 	 type here : """)
# limit = 2
# guest = 0
# false = True
# while player != keyworld and (false):
	
# 	if guest < limit:
# 		player = input("please try again: ")
# 		guest += 1
# 	else:
# 		false  = False 
    
# if false == False:
# 	print("you lose")
# else:
# 	print("you win")

# for loops: hàm liệt kê 

# for letter in "nsanflkalkdjadlkjlakdkjfkdj":
# 	print( letter)
# --------------------------
# friend =["layla","haiyo","nani"]
# for name in range(len(friend)):
# # 	print(friend[name])
# --------------------------
# number_grid = [
# [1,2,3],
# [4,5,6],
# [7,8,9],
# [0]
# ]
# -------------------------- 
# for lists in number_grid:
# 	print(lists)
# result:
# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]
# [0]
# --------------------------
# but if you use 2 for loops: 
# for lists in number_grid:
# 	for numbers in lists:
# 		print(numbers)
# result is:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 0
# That's how you list each value in a list of a list


# def translate(pharse):
# 	translation = ""
# 	for letter in pharse:
# 		if letter in "a,e,A,E":
# 			translation =translation + "g"
# 		else:
# 			translation = translation +  letter
# 	return translation
# print(translate(input("please enter the pharse: ")))



# try:
# 	value = 10/0
# 	number = int(input("please enter a number :"))
# 	print(number)
# except ZeroDivisionError as err:
# 	print(err)
# except ValueError:
# 	print("invalid number")

# Đọc file 
# =open(tên của file, hành động :r, w , a , r+)
# -.read: đọc file
# -.close: đóng file
# -.readline(): đọc từng dòng của file 

# Data = open("Data.txt", "w")
# Data.write("\nthat very nice of you")
# Data.close()




# data = open("Data.txt", "r")
# # for nice in data.readlines():
# print(data.readlines())
# data.close()




# from okna import students

# student1 = students("Jessica", "high school", 5)
# print(student1.name)






# from okna import question 


# Q = [
# "what is the color of my house? \nRed(a) \nGreen(b)\npurple(c)\nblue(d)",
# "what is the color of my patch? \nRed(a) \nGreen(b)\npurple(c)\nblue(d)",
# "what is the color of my fridge? \nRed(a) \nGreen(b)\npurple(c)\nblue(d)"
# ]

# T1 = [
# question(Q[0],"a"),
# question(Q[1],"b"),
# question(Q[2],"c"),

# ]


# def mutiple(question):
# 	score = 0
# 	for question in T1:		
# 		print("\n")
# 		player_input = input(question.question + "\nplease type your answer here: ")
# 		if player_input == question.answer:
# 			score += 1
# 	print("----------------------")
# 	print("you got " + str(score)+ "/" + str(len(T1)) + " correct answer")

# mutiple(T1)

# import random
# a = random.sample(range(1,30), 10)
# b = random.sample(range(1,30),15)

# result = [i for i in a if i in b]
# result.sort()
# print(result)


# user = int(input("type the num in here, we will check if it's a prime num or not: "))
# listrange = list(range(1, user + 1))
# divisorlist = []
# for num in listrange:
# 	if user % num == 0:
# 		divisorlist.append(num)

# def prime_num(user):
# 	if len(divisorlist) >2:
# 		print("this is not a prime num")
# 	else:
# 		print("this is a prime num")
# print("this num can be divided into", divisorlist)
# prime_num(user)



# import random
# import string

# random.choice(string.ascii_letters)
# random.sample()


num1 = 1
rangelist = list(range(1, 102))
divisorlist = []
while num1 < 100:
	for num2 in rangelist:
		if num1 % num2 == 0:
			divisorlist.append(num2)
	num1 +=1
print(divisorlist)

