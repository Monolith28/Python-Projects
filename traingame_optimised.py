import math



#this function tells you how many place values you need to express 
#regular base 10 number in your desired base
def length_of_base_num(num: int, base: int):
    exp = (num*(base-1))/base + 1
    n = math.log(exp,base)
    return math.ceil(n)

def combination_generate(instring: str, length_output: int, unique: bool):
    #instring is the list of options
    #output length is the desired number of "Place values"abs
    #unique is true if you want no replacement, false if you want with replacement

    #generate the number of possible combinations
    output_list = []
    base = len(instring)
    combinations = len(instring)**length_output
    index_list = generate_index_list(combinations, base)
    if unique == True:
        unique_indices = []
        for index in index_list:
            if check_unique(index) == True:
                unique_indices.append(index)
        index_list = unique_indices
    
    for index in index_list:
        output_list.append(index_convert(instring, index))

    return output_list





def index_convert(instring:str, index_list: list):
    opstring = ""
    for index in index_list:
        opstring += instring[index]
    return opstring

def count_base(num: int, base: int, length: int):
    base_list = []
    place_values = length
    for n in range(place_values):
        base_list.append(base**n)
    

    based_num = []

    for n in range(length):
        rev_index = length-1-n
        qty = num//base_list[rev_index]
        rem = num%base_list[rev_index]
        based_num.append(qty)
        num = rem

    return based_num



#print(index_generate(ops,4))
def generate_index_list(max_num: int, base: int):
    index_list =[]
    place_values = length_of_base_num(max_num, base)
    for n in range(max_num):
        index_list.append(count_base(n, base, place_values))
    return index_list


def check_unique(index: list):
    if len(set(index)) == len(index):
        return True
    else:
        return False


def make_unique(index_list):
    unique_index_list = []
    
    for index in index_list:
        unique_index = list(set(index))
        unique_index_list.append(unique_index)
    return unique_index_list

def specific_length(inlist: list, setlength: int):
    outlist = []
    for number in inlist:
        if len(number) == setlength:
            outlist.append(number)
    return outlist

def splice(oplist: list, codelist: list):
    eval_list = []
    for code in codelist:
        for ops in oplist:
            exp = code[0]
            for i in range(3):
                exp += ops[i] + code[i+1]
            eval_list.append(exp)

    return eval_list

            



def bracket_splice(exp: str):

    #a list of tuples. The first entry is the bracket string, the second is a
    #list of which index to insert these at in the original 14 character expression
    #When inserting these the expression becomes longer, so the new splice function
    #should iterate the subsequent indices as it inserts
    bracket_pos = [
        #1+1+1+1
        ("()",[0,3]), #(1+1)+1+1
        ("()", [4,7]), #1 +1+(1+1)
        ("(())", [0,0,3,5]), #((1+1)+1)+1
        ("(())",[2,4,7,7]), #1+(1+(1+1))
        ("()()",[0,3,4,7]), #(1+1)+(1+1)
        ("()", [2,5]) #1+(1+1)+1
    ]

    variations = []

    for situation in bracket_pos:
        b_exp = exp[:] + " " #add a space to help with bracket insertion
        b_str = situation[0] #string of brackets to insert
        b_index = situation[1] #location of brackets to insert
        i = 0
        n = 0 #shifts ll the bracket location indices as new characters inserted
        for i in range(len(b_str)):
            b_exp = b_exp[:b_index[i]+n] + b_str[i] + b_exp[b_index[i]+n:]
            i +=1
            n +=1
        variations.append(b_exp[:len(b_exp)-1])
    return variations




def remove_duplicates(soln_dic: dict):
    unique_dic = {}
    curr_exp = ""
    for exp in soln_dic:
        set_string = "".join(sorted(set(exp)))
        if set_string not in unique_dic:
            unique_dic[set_string] = exp
    return unique_dic


#code

#print(length_of_base_num(85,4))

#traincode = input("Enter a 4 digit number:")

def reach_target(code: str, target: int):
    traincode = code
    ops = "+-*/"

    all_operations = combination_generate(ops,3,False)
    all_numbers = combination_generate(traincode,4,True)
    soln = splice(all_operations, all_numbers)
    b_soln = soln[:]
    for item in soln:
        variations = bracket_splice(item)
        for variation in variations:
            b_soln.append(variation)
    realsoln = {}
    for item in b_soln:
        try:
            realsoln[item] = eval(item)
        except:
            pass

    target_dic = {}

    for item in realsoln:
        if realsoln[item] == target:
            target_dic[item] = target

    unique_dic = remove_duplicates(target_dic)
    return unique_dic

def kowalski_analysis():
    frequency_list = []
    for i in range(10000):
        missing_dig = 4-len(str(i))
        code = "0"*missing_dig + str(i)
        frequency_list.append((code,len(reach_target(code,10))))
        print(f"Testing {code}")
    return frequency_list


if __name__ == '__main__':
    results = reach_target("8917", 10)
    for item in results:
        print(f"{results[item]} = 10")
    

    """"
    analysis = kowalski_analysis()
    with open("Results.csv","w") as new_file:
        for result in analysis:
            new_file.write(f"{result[0]};{result[1]}\n")
            
    """
