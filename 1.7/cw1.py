def to_jaden_case(string):
    is_upper = True
    is_lower = False
    temp_string = ''
    for i in string:
        if is_upper:
            i = i.upper()
            temp_string += i
            is_upper = False
            is_lower = True
        elif i == ' ':
            is_upper = True
            is_lower = False
            temp_string += i
        elif is_lower:
            temp_string += i.lower()
    return temp_string


print(to_jaden_case("How can mirrors be real if our eyes aren't real"))
