def find_lost_step(equation):
    # Split the equation into left-hand side and right-hand side
    lhs, rhs = equation.split("=")
    
    for i in range(10):
        # Substitute 'x' with the current value (i) and evaluate the expression
        lhs_result = eval(lhs.replace("x", str(i)))
        rhs_result = eval(rhs)
        
        # Check if the left-hand side equals the right-hand side
        if lhs_result == rhs_result:
            return str(i)
    
    # If no solution is found, return None or raise an exception
    return None

# Test cases
print(find_lost_step("10x+2=104"))
print(find_lost_step("10-x=4"))
print(find_lost_step("1x0/3=50"))
