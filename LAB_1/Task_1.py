username = input("Enter username: ")
password = input("Enter password: ")
age = int(input("Enter age: "))
users = {
    "username": username,
    "password": password,
    "age": age    
}
print("student information:")
print("username: ",users["username"])
print("password: ",users["password"])
print("Age: ",users["age"])

if age>= 13:
    print("Account Status: Allowed")
else:
    print("Account Status: Not Allowed (Age < 13)")    
    
