import pandas as P
data= P.read_csv("student_performance.csv")
#print(data.head()) #first 5 rows
#print(data.to_string()) #to print all the data

#1 Total number of students
total_stu= len(data)
#print("The total number of students are", total_stu)

#2 students who studied more than 2 hours
gt2hr= data[data["Hours Studied"]>2]
#print(len(gt2hr)) #students who studied greater than 2 hours
#3 students who passed
stupas= data[data["Performance Index"]>35.0]
#print(len(stupas))
#4 6. Students who studied > 2 hours and passed
cond4= data[(data["Hours Studied"]>2) & (data["Performance Index"]>35.0)]
#print(len(cond4))
#5 Percentage of students who passed among those who studied > 2 hours
perc= (len(cond4)/ len(gt2hr))*100
print(perc)









