def factorize(num: int, i: int = 2, complete: bool = False, factor_list: list = [], ):
    if complete == True:
        return factor_list
    while i < num:
        if i == num:
            return factor_list
        if num%i == 0:
            factor_list.append(i)
            factorize(int(num/i), i)
        i += 1

    factor_list.append(num)
    complete = True
    return factor_list

print(factorize(18))

    