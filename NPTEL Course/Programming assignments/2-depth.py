def depth(s):
    max_depth = 0
    current_depth = 0
    for char in s:
        if char == '(':
             current_depth += 1

             if current_depth > max_depth:
                 max_depth = current_depth
                 
        elif char == ')':
            current_depth -=1
            
    return(max_depth)

result = depth("(((( (2)(3)(4)(((((((1))))))) ))))")
print(result)
    
