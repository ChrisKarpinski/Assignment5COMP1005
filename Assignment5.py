# Assignment 5
# Created by Chris Karpinski, adapted from assignment5.py starting point
# Created for: COMP1005
# Created on: Nov 2017
# This program implements searching and sorting on Student objects of the Student Class

from StudentClass import Student

def load_students(filename):

    # this function loads the csv file name into a list of students
	
    students = []
	
    file = open(filename, 'r')
	
    for line in file: 
		
	# going through each line in the file (representing the name and id of a student), instantiate a new student object by removing the new line character and splitting the data by ",". 
	line = line.strip() # strip new line characters and any whitespace from the ends of the line
	student = Student(line.split(",")[0], int(line.split(",")[1]))
	students.append(student) # append each student to the list of students

    file.close()
	
    return students

def write_students_to_file(student_list, filename):
	
    # this function writes the name and id of each student in a list of students to a specified file name (writing this information in csv format)
	
    file = open(filename, 'w')
	
    for student in student_list: 
		
	file.write(student.name + "," + str(student.id) + "\n")
	
    file.close()

def find_min_id(students): 
	
    # this function finds and returns the student object with the smallest id number in a non-empty student list
    # it is used in the implementation of the selection sort
	
    min_student = students[0]
	
    for student in students: 
		
	if student.id < min_student.id: 
			
	    min_student = student
			
    return min_student		

def sort_students_by_id(student_list):
	
    # this function implements selection sort to sort a list of students by id number
	
    for i in range(len(student_list)): 
		
	truncated_students = student_list[i:] # truncate the list according to how many elements have been sorted so far. This represents the unsorted portion of the list.
		
	min_student = find_min_id(truncated_students) # find the student with the minimum id in the unsorted portion of the students list
		
	student_list.remove(min_student) # remove the smallest id student from the list
		
	student_list.insert(i, min_student) # insert the smallest id student to the end of the growing sorted list 
		
    return student_list

def search_students_by_id(student_list, target_id):
	
    # this function uses binary search to find the index of a student in the student list with the given target id
	
    student_list = sort_students_by_id(student_list) # sort the list first to use binary search
	
    # below setting the bounds of the search space
    lower_bound_index = 0
    upper_bound_index = len(student_list) - 1
	
    while upper_bound_index >= lower_bound_index: 
		
	# while the search space is non-empty (higher bound greater than lower bound, implement the binary search algorithm)
		
	middle_index = (upper_bound_index + lower_bound_index)//2 # define the middle index as the average of the upper and lower bound indices
		
	if student_list[middle_index].id == target_id:
			
	    # if the target hits the middle id, it has been found.
			
	    return middle_index
			
	elif student_list[middle_index].id > target_id: 
			
	    # if the target is smaller than the middle id, discard the upper hallf of the list from the search space
			
	    upper_bound_index = middle_index - 1
			
	elif student_list[middle_index].id < target_id: 
			
	    # if the target is bigger than the middle id, discard the lower half of the list from the search space
			
	    lower_bound_index = middle_index + 1
	
    return -1 # target not found after search space reduced to null

def get_range_of_students(student_list, start_id, end_id):

    # this function will find the students with IDs start_id
    # and end_id and return a list of all student objects with
    # student numbers between start_id and end_id.

    # initialize the start and end indices. These are what will be the bounds of the range of the student ids if the specified start and end ids are not valid
    start_index = 0
    end_index = len(student_list) - 1
	
    if start_id > end_id: 
		
	return []
	
    if search_students_by_id(student_list, start_id) != -1: 
		
	# if the start_id is a valid id, find the index of the student in the sorted list with that id
		
	start_index = search_students_by_id(student_list, start_id)
		
		
    if search_students_by_id(student_list, end_id) != -1: 
		
	# similar to above, if the end_id is a valid id, find the index of the student in the sorted list with that id
		
	end_index = search_students_by_id(student_list, end_id)
		
    student_list = sort_students_by_id(student_list)[start_index: end_index + 1] 
    # return the slice of the list of students sorted by id according to the start and end index. If the indices of the start and end ids were not found, by default the entire list will be returned (as the default start_index and end_index initialized at the top of the function will remain unchanged)
	
    return student_list

def sort_students_by_name(student_list):
	
    # this function sorts the students according to name in descending order by using insertion sort. This follows the regular insertion sort algorithm but instead sorts from the end of the list to the beginnning of the list rather than from the beginning to the end as in regular insertion sort

    for i in range(1, len(student_list)): 
		
	listPos = len(student_list) - i - 1
		
	while listPos <= len(student_list) - 2 and student_list[listPos + 1].name > student_list[listPos].name:
			
	    tempVal = student_list[listPos]
	    student_list[listPos] = student_list[listPos + 1]
	    student_list[listPos + 1] = tempVal
	    listPos += 1

    return student_list

def search_students_by_name(student_list, target_name):
	
    # this function uses binary search on a list sorted in descending order to find the index of a student with a target name.
	
    # this binary search follows the same logic as the previous binary search above, but eliminates the upper half of the search space when the target is smaller than the middle value and vice versa for the lower half because the list is in descending order
	
    student_list = sort_students_by_name(student_list) # sort the list first (by name, in descending order)
	
    lower_bound_index = 0
    upper_bound_index = len(student_list) - 1
	
    while upper_bound_index >= lower_bound_index: 
		
	middle_index = (lower_bound_index + upper_bound_index)//2 # at each step, find the middle index of the current upper and lower bounds of the search space 
		
	if student_list[middle_index].name == target_name: 
			
	    # if the target is found at the middle index, return the middle index
			
	    return middle_index
			
	elif student_list[middle_index].name > target_name: 
			
	    # if the target is smaller than the middle value, discard the bottom half of the list from the search space (as lower values will be found at higher indices since the list is ordered in descending order)
			
	    lower_bound_index = middle_index + 1
			
	elif student_list[middle_index].name < target_name: 
			
	    # if the target is larger than the middle value, discard the top half of the list from the search space (as larger values will be found at lower indices since the list is ordered in descending order)
			
	    upper_bound_index = middle_index - 1
			
    return -1 # Not found, return -1

def main(): 

    # main is used test sample inputs/outputs when the program is run from IDE and not imported as a library.
	
    students = load_students('student_data.csv')
	
    students = sort_students_by_id(students)
	
    for i in range(len(students)): 
		
	print(students[i].id, i)
	
	
    print(search_students_by_id(students, 100573925))
    print(search_students_by_id(students, 100335718))
    print(search_students_by_id(students, 100407394))
    print(search_students_by_id(students, 100268724))
	
    students_range1 = get_range_of_students(students, 100234819, 100237231)
    students_range2 = get_range_of_students(students, 100154838, 100158715)
    students_range3 = get_range_of_students(students, 100121595, 100298802)
    students_range4 = get_range_of_students(students, 100237714, 100300860)
    students_range5 = get_range_of_students(students, 100280844, 100280445)
	
    write_students_to_file(students_range1, "output1.csv")
    write_students_to_file(students_range2, "output2.csv")
    write_students_to_file(students_range3, "output3.csv")
    write_students_to_file(students_range4, "output4.csv")
    write_students_to_file(students_range5, "output5.csv")
	
    students = sort_students_by_name(students)
	
    for i in range(len(students)): 
		
	print(students[i].name, i)	
	
    print(search_students_by_name(students, 'JEFFEREY PALTANAVAGE'))
    print(search_students_by_name(students, 'BILL MURRAY'))
    print(search_students_by_name(students, 'YOUNG WHEATCROFT'))
    print(search_students_by_name(students, 'STEVE MARTIN'))

if __name__ == "__main__": 
	
    main()


