def Plus_pass(pass_digits):
    sum_digits = 0
    for k in pass_digits:
        sum_digits += pass_digits[k]
    return sum_digits
    
    
def Pass_is_ok(pass_digits):
    if pass_digits["five"]+pass_digits["three"] == 14 and \
        pass_digits["one"] == pass_digits["two"]*2 - 1 and \
        pass_digits["four"] == pass_digits["two"] + 1 and \
        pass_digits["two"] + pass_digits["three"] == 10:
            if Plus_pass(pass_digits) == 30:
                return True


for passWord in range(0, 100000):
    this_pass = str(passWord).zfill(5)
    
    pass_digits = {}
    pass_digits["one"] = int(this_pass[0])
    pass_digits["two"] = int(this_pass[1])
    pass_digits["three"] = int(this_pass[2])
    pass_digits["four"] = int(this_pass[3])
    pass_digits["five"] = int(this_pass[4])
    
    if Pass_is_ok(pass_digits):
        print(passWord)
