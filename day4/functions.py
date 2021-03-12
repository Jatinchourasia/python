import random as rd
# print(f'{dir(random)}')   
# print(f'{rd.random()}')   

# # random1 it will print any  random value
# print(f"{rd.random()}")\
# # random2

# print(f"{rd.randint(10,20)}")

# # Random3
# print(f"{len(dir(rd.randint(10,20)))}")

# # rd.randrang(from, to ,steps)
# print(f"{rd.randrange(10,100,10)}")




# _carToDriveToday = ["Honda","maruti","hyundai"]


# rd.shuffle(_carToDriveToday)
# print(_carToDriveToday) 


# group 1

groupOne = ["india","japan","england","usa","uae","france"]
groupTwo = ["china","calafornia","italy","belgium","newyork","paru"]

# print(groupOne)
# print(groupTwo)
# numbers = list(range(len(groupOne)))
# rd.shuffle(groupOne)
# rd.shuffle(groupTwo)
# print(groupOne)
# print(groupTwo)

# # # print(numbers)
# for i in numbers:
# 	print(groupOne[i], "vs",groupTwo[i])

# range
# print(range()) ==> error rnge need atleast one parameter
# for value in range(5):
# 	print(value)

# print(f"{list(range(+5))}")
# two parameter in rtsnge
# print(f"{list(range(2,5))}")
# print(f"{list(range(-2,5))}")

# interval
# print(f"{list(range(1,10,2))}")
# range function never go backwards
# ]not working because interval is incrementing
# print(f"{list(range(10,1,2))}")
# # when interval is decrimented
# print(f"{list(range(10,1,-2))}")

# #----------------------------------------------------FILTER METHOD--------------------------------------
# # we can only pass one parameter in filter which is itratable
# findMovies =["movie1", "movie2","movie5"]

# def filterMovies(movies):
# 	movieLibrary = ["movie1", "movie2","movie6", "movie5","movid6", "movie9"]
# 	if(movies in movieLibrary):
# 		return True
# 	else:
# 	 return False	

# # filter(method,object(eg.. findmovies))
# group = ["movie1", "movie2","movie6", "movie5","movid6", "movie9"]
# rd.shuffle(group)

# randomMovie = [group[1],group[2]]

# filterMovieObject = filter(filterMovies, randomMovie)
# print(type(filterMovieObject))
# print(f"{filterMovieObject}")

# # for _movie in filterMovieObject:
# # 	print(_movie)


# # --------------------------------------------------------MAP FUNCTION------------------------------------------------

# def agrigate(marks):
# 	return (marks/400)*100

# # precentage

# def percentage(marks,totalMarks):
# 	return (marks/totalMarks)*100
# yearMarks = (800,700,900,1000)
# totalMarks=(1000,1000,1500,2000)
# resultMapObject= map(percentage,yearMarks,totalMarks)
# result = list(resultMapObject)
# # degree = map()

# number = len(result)
# avgMark = 0
# for marks in result:
# 	avgMark = avgMark+marks

# print(agrigate(avgMark))


# -----------------------------------------------------------ZIP FUNCTION--------------------------------------------
firstName =("kaushal","yash","jyoti","ishan")
middleName =("h","s","k","a")
lastName =("kesari","rajoria","tiwari","khan")
course = ("IT","CS","EC","ME")

# size should be same or it will zip the smallest size only
zipObject = zip(firstName,middleName,lastName)
zipObject2 =zip(firstName,middleName,lastName)


tupleZipObject = tuple(zipObject)


for value in tupleZipObject:
	print(value)

print(type(tupleZipObject))

