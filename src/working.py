"""
given a list of students and their scores, write a function that returns the avg
of each student's top five scores, in ascending order of student id 

UNDERSTAND:
- we have a list of lists in this scenario 
- gather the top five scores for each student and avg them


PLAN:
- make a dict with student id as the key and scores as the value  


"""


def student_avg(scores):
    #define dict 
    students_to_scores = {}
    
    # for each item in the list of list
    for elem in scores:
        # define the student id and score from list item 
        student_id = elem[0]
        score = elem[1]
        
        # check to see if the student id exists in the dict yet 
        if student_id not in students_to_scores:
            # if not, generate a spot in the dict to hold scores
            students_to_scores[student_id] = []
        
        student_scores = students_to_scores[student_id]
        student_scores.append(score)
    
    # sort the students in the dict by their ids  
    sorted_students_ids = sorted(students_to_scores.keys())

    # sort each of the scores for each student
    for student_id in sorted_students_ids:
        sorted_scores = sorted(students_to_scores[student_id])
        
        # get the top five by slicing 
        top_five = sorted_scores[-5:]

        average = sum(top_five) // len(top_five)

        top_five_avgs.append([student_id, average])


def csAverageOfTopFive(scores):
    # scores is a list of lists
    # each inner list has two elements: inner[0] = student id
    #                                   inner[1] = score
    # gather the top 5 scores for each student and average them
    # make a dict with student id as key and scores as the value
    students_to_scores = {} # key: student id, value is list of scores
    for elem in scores: 
        student_id = elem[0]
        score = elem[1]
        if student_id not in students_to_scores: 
            students_to_scores[student_id] = []
        student_scores = students_to_scores[student_id]
        student_scores.append(score)
    sorted_student_ids = sorted(students_to_scores.keys())
    top_five_averages = []
    print(sorted_student_ids)
    for student_id in sorted_student_ids: # O(n) where n is number of unique students
        sorted_scores = sorted(students_to_scores[student_id], reverse=True) # O(n log n) where n is num of scores for student
        top_five = sorted_scores[:5]
        print("top_five", top_five)
        average = sum(top_five) // len(top_five)
        top_five_averages.append([student_id, average])
    return top_five_averages