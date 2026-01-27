def salary(sal):
    HRA = sal * 0.1
    DA = sal * 0.05
    return s + HRA + DA
sal = float(input("Enter basic salary: "))
total_salary = salary(sal)
print("Total salary:", total_salary)
