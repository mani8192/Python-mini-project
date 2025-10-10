# student_grade_calculator--

# 1-fuṇction --
def student_grade_calculator():
    print(f'welcome ->')
    
# 2 -student name --
    s_name = input("Enter a student name:-")
    
# 3 student subject  marks --
    subject = int(input("How many subject marks :-"))
    
    total_marks = [] 
    for i in range(1 , subject + 1):
        s_marks = int(input(f"Enter a marks number{i} :-"))
        total_marks.append(s_marks)
        
# 4 - total - parcentage --
        
        total = sum(total_marks) # sum of total marks 
        max_marks = subject * 100  
        marks_percentage = (total / max_marks) * 100
        
# 5 - condition 
        
        if marks_percentage >= 80:
            print('Gread A')
            
        elif marks_percentage >= 60:
            print('Gread B')
            
        elif marks_percentage >= 50:
            print('Gread C')
            
        elif marks_percentage >= 33:
            print('You are pass')
            
        else:
            print('you fail ')
    
    
# 6 print --
    print(f"student name,{s_name} \n student marks {s_marks} \n total marks -{total} \n maximum {max_marks} \n marks-percentage{marks_percentage}")
    
        
    
student_grade_calculator()