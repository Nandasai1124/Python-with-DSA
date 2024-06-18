try:
    
    print("Open File")
    result=10/0
except ZeroDivisionError:
    print("Cannot divide by zero!")
    
else:
    print("Division successful,result:",result)
finally:
    print("Close")
    print("Execution Completed")