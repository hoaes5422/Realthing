# #hello every one
# name = set()
# name.add(1)
# name.add(2)
# name.add(3)
# name.add(4)
# name.add(3)
# print(name)

# print(f"the name have {len(name)} elements")

# for num in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]:
# 	print(num)



# for x in range(105):
# 	print(x)

# names = ["harry","potter","witch","hayla"]
# for x in names:
# 	print(x)

# name = "Hubert Blaine Wolfeschlegelsteinhausenbergerdorff"

# for y in name:
# 	print(y)


# def square(x):
# 	return x*x
	

# for n in range(10):
# 	print(f"the square of {n} is {square(n)}")



# class student:
# 	def __init__(self, name, age ,gpa, house):
# 		self.name = name
# 		self.age = age
# 		self.gpa = gpa
# 		self.house = house

# student1 = student("Richard", str(16) + " yearl olds", 8,"NY")

# print(student1.name)
# print(student1.house)
# print(student1.age)
# print(student1.gpa)





# class Flight:

# 	def __init__(self, blank):
# 		self.blank	= blank
# 		self.passengers_list = []

		
# 	def add_passengers(self,name):
# 		if not self.seat() :
# 			return False
# 		self.passengers_list.append(name)
# 		return True
	
# 	def seat(self):
# 		return self.blank - len(self.passengers_list)


# flight = Flight(3)

# people = ["harry","nani","bop","emerland"]

# for person in people: 
# 	if flight.add_passengers(person):
# 		print(f"add {person} into the flight successfully.")
# 	else:
# 		print(f"not enough space for {name}")



# def annouce(f):
# 	def wrapper():
# 		print("About to run the fuction...")
# 		f()
# 		print("done with the fuction.")
# 	return wrapper
# @annouce
# def hello():
# 	print("HELLO WORLD WE ARE HERE")

# hello()


# people = [ 
# 	{"Bye":"Draco","names":"sort of thing "},
# 	{"hello":"layla","names":"thing of thing"},
# 	{"nothing":"nope","names":"thing and things"}
# ]

# try:
# 	people.sort(key= lambda person: person["names"])
# except:
# 	print("this is not a right thing to do")

# print(people)


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

