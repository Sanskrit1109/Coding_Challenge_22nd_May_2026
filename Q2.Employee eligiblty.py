# A company wants to identify whether an employee is eligible for a bonus based on attendance percentage andperformance rating.

print("Enter the attendence percentage :")
attendance = float(input())
print("Enter the performance rating (1-5) :")
performance_rating = int(input())
if attendance >= 90 and performance_rating >= 4:
    print("Employee is eligible for bonus")
else:
    print("Employee is not eligible for bonus")

# Output 1
#Enter the attendence percentage :
#80
#Enter the performance rating (1-5) :
#4
#Employee is not eligible for bonus

#Output 2
#Enter the attendence percentage :
#95
#Enter the performance rating (1-5) :
#4
#Employee is eligible for bonus