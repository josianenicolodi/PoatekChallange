'''using a tupla to deal with the variables no mutables 
deal with a varible to do a media of  height of the students 

'''




students=(("Bruno", 170, 14), ("Leonardo", 174, 21), ("Juan", 156, 12), ("Juliana", 166, 13), ("Wagner",
184, 17), ("Micaela", 172, 18), ("Bento", 150, 14), ("Lucia", 162, 13), ("Pedro", 169, 14), ("Carla",
158, 16)) 

totalHeight = 0
for x in range(len(students)):
    totalHeight+= students[x][1]
averageHeight = totalHeight / len(students)
print("average height: %d" % averageHeight)
higher_than_13 = tuple(element for element in students if element[2] > 13 and element[1] < averageHeight)
print("The students 13+ smaller than average height are: ")
print(higher_than_13)


