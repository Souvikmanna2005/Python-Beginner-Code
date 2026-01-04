def give_raise(employee_dict):

    print("Original employee salaries:")
    print(employee_dict)
    
    for employee in employee_dict:
        employee_dict[employee] *= 1.10  # Increase salary by 10%
    
    print("Updated employee salaries (10% raise applied):")
    print(employee_dict)

employees = {
    "Alice": 50000,
    "Bob": 60000,
    "Charlie": 45000
}

give_raise(employees)


"""  
10% = 10/100 = 0.10
To increase by 10%: 100% + 10% = 110% = 1.10

"""
