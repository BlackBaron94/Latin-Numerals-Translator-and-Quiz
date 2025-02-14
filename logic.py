from random import randint

class number:
    
    def __init__(self, latin, decimal):
        self.latin = latin
        self.decimal = decimal
        
    def return_value(self):
        return self.decimal

def initialize():
    # Creates numerals classes and array
    i = number('I', 1)
    v = number('V', 5)
    x = number('X', 10)
    l = number('L', 50)
    c = number('C', 100)
    d = number('D', 500)
    m = number('M', 1000)
    global numerals
    numerals = [i,v,x,l,c,d,m]

    # A nice correct guess global counter
    global quiz_streak
    quiz_streak = 0
    
def randomize():
    # Decides Latin to Decimal or vice versa
    random_type = randint(0,1)
    
    random_number = randint(0,3999)
    # 0 == Requests Decimal to Latin
    if random_type:
        return str(random_number)
    # 1 == find out Latin version, request Latin to Decimal
    else: 
        random_latin = dec2lat(random_number)
        return random_latin
    
    

# Retains only latin numerals present in string
def purify_input(input_string):
    purified_string = ''
    for letter in input_string:
        letter = str(letter).capitalize()
        if letter not in "IVXLCDM":
            continue
        else:
            purified_string = purified_string + letter
    
    return purified_string

def letter_conversion(letter):
    # Handles "None" case
    if letter:
        for y in numerals:
            if letter == y.latin:
                return y.return_value()
    else:
        return 0
    
# Returns a list, 
# [0] is a mistake flag    
# If return array len = 2, [1] = VLD letter that was used in a wrong way
# If return array len = 3, [1] = letter that doesn't have required 1/10 value
# [2] = letter whose value is higher than [1] * 10.
def lat2dec(my_num):
    my_num = purify_input(my_num)
    
    # If string doesn't contain any numerals
    if len(my_num) == 0:
        return [False, False]
    
    # Checks if same numeral appears more than 3 times
    same_letter = 0
    for index in range(0, len(my_num)-1):
        # Exception for 4000+ taking lack of V̅ into consideration
        if my_num[index] == my_num[index+1] and my_num[index] != 'M':
            same_letter += 1
        # Counter needs to reset to allow numbers like XXXIX = 39
        else:
            same_letter = 0
        if same_letter > 2:
            return [False, my_num[index]]
        
        
    my_sum = 0
    index = 0
    while index < len(my_num):
        current_value = letter_conversion(my_num[index])
        # Checks if VLD are repeated
        if (int(current_value) in (500,50,5) ):
            i = index + 1
            while i <= len(my_num) - 1:
                if my_num[index] == my_num[i]:
                    return [False, my_num[index]]
                i += 1

        
        # Check if current letter is the last letter
        # If it's not, calculates next letter
        if index != (len(my_num) - 1 ):
            next_letter = my_num[index + 1]
        
        # If it is, next_letter = none 
        
        else:
            next_letter = None
        
        # Returns value from letter_conversion (0 if None)
        next_value = letter_conversion(next_letter)
        
        # Checks for IV, IX etc reductions of V/X/... values by I/X/... values
        if current_value < next_value:
            
            # Checks if VLD are placed before an XCM respectively
            if ( int(current_value / 5) in (100,10,1) ) and (current_value < next_value):
                return [False, my_num[index]]
            
            # Checks wrongful use, e.g. IC or VM
            if ( (next_value != 0) and (current_value/next_value < 0.1) ):
                return [False, my_num[index], my_num[index+1]]
            
            # Checks if previous letter was also same letter, which is
            # a mistake for a reduction case, like XIIX
            # Makes sure current letter is not first one, or else it would
            # compare to last letter ( array [-1] )
            if (my_num[index-1] == my_num[index]) and (index != 0):
                return[False, my_num[index]]
            
            
            try:    
                # Checks for IXI/XCX etc
                if (my_num[index+2] == my_num[index]):
                    return[False, my_num[index]]
                # Checks for IXV/XCL/XIVM/IVD etc
                elif (letter_conversion(my_num[index+2]) > current_value):
                    return[False, my_num[index+2]]
            # No harm done by *pass* in this case, mistake is impossible
            except IndexError:
                pass
            
            # Increases sum by V-I = 4, X-I = 9 etc
            my_sum = my_sum + (next_value - current_value)
            
            # If next letter isn't the last one
            if index+1 < len(my_num) - 1:
                # Skip next letter 
                # Example
                # (for IV, (V-I) is already calculated,
                # V shouldn't be counted again)
                index += 2
                continue
            
            # If next letter is last one, calculation is done already
            else:
                break
            
        # If next value is less than current, current needs to be added
        # and next to be checked in its own iteration
        else:
            my_sum = my_sum + current_value
            index += 1
            
    return [True, my_sum]

# Translates decimals to latin
def dec2lat(my_num_str):
    # Tries to get an integer out of input string
    try:
        my_num_int = int(my_num_str)
    # If input string contains non-decimals
    except:
        return False
    
    # *THIS WORKS UP TO 3999*
    digits = []
    divider = 1000
    latin = ''
    # Grabs each digit by dividing seperately, if none, grabs 0
    # 1st iteration [0]/1000, 2nd [1]/100 etc
    for index in range(0,4):
        # Division and addings digit
        digits.append(int(my_num_int // divider))
        # Reduces main number by digit * place, e.g. if [0] was 4, then -4*1000
        my_num_int = my_num_int - digits[index] * divider
        # Reduces divider for next iteration from 10^x to 10^x-1
        divider = divider / 10
    
    # Thousands are calculated differently due to limitations
    # E.g. 4000 = MMMM instead of MV̅ due to character limitations
    if digits[0]:
        latin +=  (numerals[-1].latin * digits[0])
    
    # Rest of the digits are calculated through digit_conversion()
    for index in range(1,4):
        # Zeros are handled here
        if digits[index]:
            latin += digit_conversion(digits, index)
    return latin

# Converts a certain digit to the corresponding latin numeral(s)
def digit_conversion(digits_array, digit_num):
    return_string = ''
    
    # digit 1 base value 100, 
    # digit 2 base value 10, 
    # digit 3 base value 1
    
    # Calculates which base value applies for current digit_num
    # e.g. if the digit_num(index) is 3, 
    # then the number has base value 10^0 = 1
    base_value = pow(10,(3-digit_num))
    
    # Subset to be used for this particular digit
    subset = []
    
    # Subset[0] is base_value
    # Checks which numeral has the base value we're looking for, I/X/C
    for numeral in numerals:
        if numeral.decimal == base_value:
           subset.append(numeral)
           break
       
    # Subset[1] is used in case of digit being a 9, 
    # e.g. X base value requiring C to depict 90, XC
    for numeral in numerals:
        if numeral.decimal == base_value*10:
           subset.append(numeral)
           break
       
    # Subset[2] is used in case of digit being "near" a 5, 
    # e.g. X base value requiring L to depict 60, LX
    for numeral in numerals:
        if numeral.decimal == base_value*5:
           subset.append(numeral)
           break

    # Checks examined digit
    if digits_array[digit_num] == 9:
        # Appends to string the numeral that's given by x, x*10 like IX, XC, CM
        return_string = return_string + subset[0].latin
        return_string = return_string + subset[1].latin
    
    elif digits_array[digit_num] >= 5:
        # Since it's >= 5 we definetely need subset[2] first (V,L,D)
        return_string = return_string + subset[2].latin
        # If it's > 5, we need to append base value X times, where X = number-5
        # e.g. if number is 7, we need to append base value 7-5=2 times e.g. DCC
        if digits_array[digit_num] > 5:
            return_string = return_string + (subset[0].latin * (digits_array[digit_num] - 5))
    
    elif digits_array[digit_num] == 4:
        # 4 requires special handling as it's the only case where base_value is 
        # placed right before subset[2] (IV, XL, CD)
        return_string = return_string + subset[0].latin
        return_string = return_string + subset[2].latin
    
    # Basically when <= 3, append base value * number.
    else:
        return_string = return_string + (subset[0].latin * digits_array[digit_num])
    return return_string 

initialize()