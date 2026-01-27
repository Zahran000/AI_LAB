def salary(sal):
    HRA = s * 0.1
    DA = s * 0.05
    return s + HRA + DA
sal = float(input("Enter basic salary: "))
total_salary = salary(sal)
print("Total salary:", total_salary)
