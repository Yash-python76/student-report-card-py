import time

print("================WELCOME! TO STUDENT REPORT CARD.===============")
name = input("Enter student name :")
cls_1 = int(input("Enter your class you're studying in :"))
stream = input("Enter your current stream :")
if stream.lower() == "science":
    print("Great you're studying in science stream",name)
    physics = int(input("Enter your physics marks :"))
    chemistry = int(input("Enter your chemistry marks :"))
    maths = int(input("Enter your maths marks :"))
    bio = int(input("Enter your biology marks :"))
    total = physics+chemistry+maths+bio
    percentage = (total/400)*100
    print("Calculating your total marks and percentage.........")
    time.sleep(3) #3 secound wait
    print("Total marks is :",total)
    print("Percentage(%) is :",percentage)
elif stream.lower() == "commerce":
    print("Great you're studying in commerce stream",name)
    Book_1 = int(input("Enter your Book keeping marks :"))
    acc = int(input("Enter accountancy marks :"))
    ocm = int(input("Enter OCM marks :"))
    maths = int(input("Enter maths marks :"))
    total_1 = Book_1+acc+ocm+maths
    percentage = (total_1/400)*100
    print("Calculating your total marks and percentage.......")
    time.sleep(3) #3 secound wait
    print("total marks is:",total_1)
    print("Percentage(%) is",percentage)
elif stream.lower() == "arts":
    print("Great you're studying in arts stream",name)
    history = int(input("Enter your history marks :"))
    geo = int(input("Enter geography marks :"))
    poli_sci = int(input("Enter political science marks :"))
    maths = int(input("Enter maths marks :"))
    total_1 = history+geo+poli_sci+maths
    percentage = (total_1/400)*100
    print("Calculating your total marks and percentage.......")
    time.sleep(3) #3 secound wait
    print("total marks is:",total_1)
    print("Percentage(%) is",percentage)
else:
    print("Incorrect stream please try again!!☹️")
    exit()
#User grade with overall report card
print("-----STUDENT GRADE CRITERIA----")
print("Grade O = 100 to 90\nGrade A+ = 80 to 89\nGrade A = 70 to 79\nGrade B = 60 to 69\nGrade C = 50 to 59\nGrade D = 40 to 49")
print("Dear user😊!! Hope so your percentage is perfect let's Analize your grade..")
grade_1 = float(input("Enter your percentage :"))
if(grade_1>=90):
    print("Outstanding...! you got grade O",name)
elif(grade_1>=80):
    print("Excellent....! you got grade A+",name)
elif(grade_1>=70):
    print("Very Good...! you got grade A",name)
elif(grade_1>=60):
    print("Good....! you got grade B",name)
elif(grade_1>=50):
    print("Nice...! you got grade C",name)
elif(grade_1>=40):
    print("You can do it better next time..! you got grade D")
else:
    print("Unfortunately your grade is not in criteria☹️!!Apply for Re-exam")
    print("Result = Fail")
    exit()
print("-------------------YOUR OVERALL REPORT CARD/SCORE CARD.--------------------")
if stream.lower() == "science":
    print("Name of candidate :",name)
    print("Class of candidate :",cls_1)
    print("Stream of candidate :",stream)
    print("Total marks of candidate :",total)
    print("Total percentage of candidate :",percentage)
    print("Result = Pass")
elif stream.lower() =="commerce":
    print("Name of candidate :",name)
    print("Class of candidate :",cls_1)
    print("Stream of candidate :",stream)
    print("Total marks of candidate :",total_1)
    print("Total percentage of candidate :",percentage)
    print("Result = Pass")
elif stream.lower() =="arts":
    print("Name of candidate :",name)
    print("Class of candidate :",cls_1)
    print("Stream of candidate :",stream)
    print("Total marks of candidate :",total_1)
    print("Total percentage of candidate :",percentage)
    print("Result = Pass")
else:
    print("Due to incorrect information please try again....!")
