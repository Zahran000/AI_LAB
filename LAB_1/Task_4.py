def salary(s):
    HRA = s * 0.1
    DA = s * 0.05
    return s + HRA + DA
s = float(input("Enter basic salary: "))
total_salary = salary(s)
print("Total salary:", total_salary)
