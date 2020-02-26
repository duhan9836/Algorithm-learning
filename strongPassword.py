def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    types=[numbers,lower_case,upper_case,special_characters]
    types_contained=[]
    for s in password:
        for t in types:
            if len(types_contained)<4:
                if s in t and t not in types_contained:
                    types_contained.append(t)
    print(types_contained)
    num_of_types=len(types_contained)
    num_in_need = max(4-num_of_types,6-n,0)
    return num_in_need

print(minimumNumber(3,"Ab1"))