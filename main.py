import decimal

################################# VARIABLE DECLARATIONS ############################################

is_valid = False
is_complete = False
hex_characters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]

####################################### FUNCTIONS ##################################################

# Decimal to binary conversion.
def decimal_to_binary(value):
    # FUNCTION VARIABLES
    is_negative = False
    binary_fraction_places = 0
    fraction_mult = 0.5
    binary_string = ""
    decimal_places = 0

    # Determine if value is negative for 2's complement later and convert to absolute value.
    value = float(value)

    if value < 0:
        is_negative = True
        value = value * -1

    value = str(value)

    # The fractional value is separated from the integer value
    # Decimal places are store to ensure no issues with floating point arithmetic.
    decimal_fraction = decimal.Decimal(value)
    decimal_fraction_places = abs(decimal_fraction.as_tuple().exponent)
    decimal_fraction = float(decimal_fraction)
    decimal_fraction = float(decimal_fraction % 1)
    decimal_fraction = round(decimal_fraction, decimal_fraction_places)

    # Since the fractional value is stored, value can be stored as an integer.
    value = int(float(value))

    # Fraction conversion
    while decimal_fraction != 0:
        if decimal_fraction / fraction_mult >= 1:
            binary_string = binary_string + "1"

            # Fraction value converted for precise floating point arithmetic and rounding.
            decimal_fraction = decimal.Decimal(decimal_fraction)
            decimal_fraction_places = abs(decimal_fraction.as_tuple().exponent)
            decimal_fraction = float(decimal_fraction)
            decimal_fraction = float(decimal_fraction - fraction_mult)
            decimal_fraction = round(decimal_fraction, decimal_fraction_places)
        else:
            binary_string = binary_string + "0"
        fraction_mult = fraction_mult / 2

    if binary_string == "":
        binary_string = "0"
    binary_string = "." + binary_string

    # Integer conversion
    while value != 0:
        if value % 2 == 1:
            binary_string = str("1") + binary_string
        else:
            binary_string = str("0") + binary_string
        value = int(value / 2)

    # 2's compliment conversion
    if is_negative:
        temp_string = ""
        decimal_places = 0

        # Flip all the bits
        for i in range(0, len(binary_string)):
            if binary_string[i] == "0":
                temp_string = temp_string + "1"
            elif binary_string[i] == "1":
                temp_string = temp_string + "0"
            elif binary_string[i] == ".":
                decimal_places = len(binary_string) - i - 1
        temp_string = "1" + temp_string

        # Add 1 to the right-most bit and reformat number
        temp_string = bin(int(temp_string, 2) + int("1", 2))
        temp_string = str(temp_string)

        temp = ""

        # Re-insert decimal
        for i in range(0, len(temp_string)):
            if i < len(temp_string) - 2:
                if i == decimal_places:
                    temp = "." + temp
                temp = temp_string[len(temp_string) - 1 - i] + temp
        binary_string = temp
    else:
        binary_string = "0" + binary_string

    return binary_string

# Decimal to Hexadecimal Conversion
def decimal_to_hexadecimal(value):
    # FUNCTION VARIABLES
    is_negative = False
    hex_fraction_places = 0
    hex_string = ""
    decimal_places = 0

    # Determine if value is negative for 16's complement later and convert to absolute value.
    value = float(value)

    if value < 0:
        is_negative = True
        value = value * -1

    value = str(value)

    # The fractional value is separated from the integer value
    # Decimal places are store to ensure no issues with floating point arithmetic.
    decimal_fraction = decimal.Decimal(value)
    decimal_fraction_places = abs(decimal_fraction.as_tuple().exponent)
    decimal_fraction = float(decimal_fraction)
    decimal_fraction = float(decimal_fraction % 1)
    decimal_fraction = round(decimal_fraction, decimal_fraction_places)

    # Since the fractional value is stored, value can be stored as an integer.
    value = int(float(value))

    # Fraction conversion
    while decimal_fraction != 0:
        temp = int(decimal_fraction * 16)
        decimal_fraction = (decimal_fraction * 16) - temp
        hex_string = hex_string + hex_characters[temp]

    if hex_string == "":
        hex_string = "0"
    hex_string = "." + hex_string

    # Integer conversion
    while value != 0:
        hex_string = hex_characters[value % 16] + hex_string
        value = int(value / 16)

    hex_string = "0" + hex_string

    # 16's compliment conversion
    if is_negative:
        temp_string = ""
        decimal_places = 0

        # Flip all the bits and add 1
        temp_string = ""
        for i in range(0, len(hex_string)):
            if hex_string[i] == ".":
                decimal_places = len(hex_string) - i - 1
            else:
                temp = hex(int("F", 16) - int(hex_string[i], 16))
                temp_string = temp_string + temp[2]
        temp_string = hex(int(temp_string, 16) + int("1", 16))

        # Merge strings together and remove hex indicator.
        hex_string = ""
        for i in range(0, len(temp_string)):
            if i == len(temp_string) - decimal_places:
                hex_string = hex_string + "." + temp_string[i]
            else:
                hex_string = hex_string + temp_string[i]
        temp_string = ""
        for i in range(0, len(hex_string)):
            if i > 1:
                temp_string = temp_string + hex_string[i]
        hex_string = temp_string

    # Format the string to all caps and return
    hex_string = hex_string.upper()
    return hex_string

# Binary to Decimal
def binary_to_decimal(value):
    # Function variables
    decimal_places = 0
    fraction_string = ""
    integer_string = ""
    is_integer = True
    is_negative = False
    decimal_string = ""
    integer_value = 0
    fraction_value = 0
    decimal_value = 0

    # determine whether value is positive or negative and remove first bit
    if value[0] == "1":
        is_negative = True
    temp_string = ""
    for i in range(1, len(value)):
        temp_string = temp_string + value[i]
    decimal_string = temp_string

    # The fractional value is separated from the integer value
    for i in range(0, len(decimal_string)):
        if decimal_string[len(decimal_string) - i - 1] == ".":
            decimal_places = i
            is_integer = False
            fraction_string = integer_string
            integer_string = ""
        else:
            integer_string = decimal_string[len(decimal_string) - i - 1] + integer_string

    # If negative, flip the bits and add 1
    if is_negative == True:
        temp_string = ""
        for i in range(0, len(integer_string)):
            if integer_string[i] == "0":
                temp_string = temp_string + "1"
            elif integer_string[i] == "1":
                temp_string = temp_string + "0"
        integer_string = temp_string
        temp_string = ""
        for i in range(0,len(fraction_string)):
            if fraction_string[i] == "0":
                temp_string = temp_string + "1"
            elif fraction_string[i] == "1":
                temp_string = temp_string + "0"
        fraction_string = temp_string

        # Merge strings together and perform 2's compliment.
        temp_string = integer_string + fraction_string
        temp_string = bin(int(temp_string, 2) + int("1", 2))

        # Separate integer from fraction again.
        fraction_string = ""
        integer_string = ""
        for i in range(0, len(temp_string)):
            if i < decimal_places:
                fraction_string = temp_string[len(temp_string) - 1 - i] + fraction_string
            elif i < len(temp_string) - 2:
                integer_string = temp_string[len(temp_string) - 1 - i] + integer_string

    # Convert integer first, then the fraction.
    for i in range(0, len(integer_string)):
        integer_value = integer_value + (int(integer_string[i]) * 2 ** (len(integer_string) - i - 1))

    for i in range(0, len(fraction_string)):
        fraction_value = float(fraction_value + float(int(fraction_string[i]) * 0.5 ** (i + 1)))

    # Add integer and fraction values, and if negative, multiply by -1.
    decimal_value = float(integer_value + fraction_value)
    if is_negative:
        decimal_value = decimal_value * -1
    decimal_string = str(decimal_value)

    return decimal_string

# Hexadecimal to Decimal
def hexadecimal_to_decimal(value):
    # Function variables
    decimal_string = ""
    is_negative = False
    temp_string = ""
    integer_string = ""
    fraction_string = ""
    decimal_places = 0
    is_integer = True

    # determine whether value is positive or negative and remove first bit if negative
    if value[0] == "F":
        is_negative = True
        for i in range(1, len(value)):
            temp_string = temp_string + value[i]
    else:
        temp_string = value

    # The fractional value is separated from the integer value
    for i in range(0, len(temp_string)):
        if temp_string[len(temp_string) - i - 1] == ".":
            decimal_places = i
            is_integer = False
            fraction_string = integer_string
            integer_string = ""
        else:
            integer_string = temp_string[len(temp_string) - i - 1] + integer_string

    # If negative, flip the bits and add 1
    if is_negative == True:
        temp_string = ""
        temp = ""
        for i in range(0, len(integer_string)):
            temp = hex(int("F", 16) - int(integer_string[i], 16))
            temp_string = temp_string + temp[2]
        integer_string = temp_string
        temp_string = ""
        temp = ""
        for i in range(0, len(fraction_string)):
            temp = hex(int("F", 16) - int(fraction_string[i], 16))
            temp_string = temp[2] + temp_string
        fraction_string = temp_string

        # Merge strings together and perform 2's compliment.
        temp_string = integer_string + fraction_string
        temp_string = hex(int(temp_string, 16) + int("1", 16))

        # Separate integer from fraction again.
        fraction_string = ""
        integer_string = ""
        for i in range(0, len(temp_string)):
            if i < decimal_places:
                fraction_string = temp_string[len(temp_string) - 1 - i] + fraction_string
            elif i < len(temp_string) - 2:
                integer_string = temp_string[len(temp_string) - 1 - i] + integer_string

    integer_string = integer_string.upper()
    fraction_string = fraction_string.upper()

    # Convert hex to numeric values
    temp_integer_values = [0] * len(integer_string)
    for i in range (0, len(integer_string)):
        if integer_string[i] == "A":
            temp_integer_values[i] = 10
        elif integer_string[i] == "B":
            temp_integer_values[i] = 11
        elif integer_string[i] == "C":
            temp_integer_values[i] = 12
        elif integer_string[i] == "D":
            temp_integer_values[i] = 13
        elif integer_string[i] == "E":
            temp_integer_values[i] = 14
        elif integer_string[i] == "F":
            temp_integer_values[i] = 15
        else:
            temp_integer_values[i] = int(integer_string[i])
    temp_fraction_values = [0] * len(fraction_string)
    for i in range (0, len(fraction_string)):
        if fraction_string[i] == "A":
            temp_fraction_values[i] = 10
        elif fraction_string[i] == "B":
            temp_fraction_values[i] = 11
        elif fraction_string[i] == "C":
            temp_fraction_values[i] = 12
        elif fraction_string[i] == "D":
            temp_fraction_values[i] = 13
        elif fraction_string[i] == "E":
            temp_fraction_values[i] = 14
        elif fraction_string[i] == "F":
            temp_fraction_values[i] = 15
        else:
            temp_fraction_values[i] = int(fraction_string[i])

    # Convert integer first, then the fraction.
    integer_value = 0
    fraction_value = 0
    for i in range(0, len(integer_string)):
        integer_value = integer_value + (temp_integer_values[i] * 16 ** (len(integer_string) - i - 1))
    for i in range(0, len(fraction_string)):
        fraction_value = float(fraction_value + float(temp_fraction_values[i] * 0.0625 ** (i + 1)))

    # Add integer and fraction values, and if negative, multiply by -1.
    decimal_value = float(integer_value + fraction_value)
    if is_negative:
        decimal_value = decimal_value * -1
    decimal_string = str(decimal_value)

    return decimal_string

#################################### USER INPUT OPTIONS ############################################

while not is_complete:
    is_valid = False

    while not is_valid:
        input_type = input("What kind of number do you want to convert?\n1. Decimal\n2. Binary\n3. Hexadecimal\n")
        if input_type == "1" or input_type == "2" or input_type == "3":
            is_valid = True
        else:
            print("INVALID")

    is_valid = False

    while not is_valid:
        convert_type = input("What would you like to convert to?\n1. Decimal\n2. Binary\n3. Hexadecimal\n")
        if convert_type == "1" or convert_type == "2" or convert_type == "3":
            is_valid = True
        else:
            print("INVALID")

    is_valid = False

    while not is_valid:
        input_value = input("Enter a valid number/value: ")
        invalid_characters = 0
        total_decimals = 0
        total_negatives = 0

        # Check to make sure input is valid before converting. Hex characters must be capitalized.
        if input_type == "1":
            for i in range(0, len(input_value)):
                if not input_value[i].isnumeric():
                    if input_value[i] == ".":
                        total_decimals = total_decimals + 1
                    elif input_value[i] == "-":
                        total_negatives = total_negatives + 1
                    else:
                        invalid_characters = invalid_characters + 1
            if invalid_characters == 0 and total_decimals <= 1 and total_negatives <= 1:
                is_valid = True
            else:
                print("INVALID")
        elif input_type == "2":
            for i in range(0, len(input_value)):
                if not (input_value[i] == "0" or input_value[i] == "1"):
                    if input_value[i] == ".":
                        total_decimals = total_decimals + 1
                    else:
                        invalid_characters = invalid_characters + 1
            if invalid_characters == 0 and total_decimals <= 1:
                is_valid = True
            else:
                print("INVALID")
        elif input_type == "3":
            for i in range(0, len(input_value)):
                if not input_value[i].isnumeric() and input_value[i] != "A" and input_value[i] != "B" and input_value[i] != "C" and input_value[i] != "D" and input_value[i] != "E" and input_value[i] != "F":
                    if input_value[i] == ".":
                        total_decimals = total_decimals + 1
                    else:
                        invalid_characters = invalid_characters + 1
            if invalid_characters == 0 and total_decimals <= 1:
                is_valid = True
            else:
                print("INVALID")

    ###################################### CONVERSIONS #################################################

    if input_type == "1":
        if convert_type == "1":
            print("Decimal: " + input_value)
        elif convert_type == "2":
            print("Binary: " + decimal_to_binary(input_value))
        elif convert_type == "3":
            print(" Hexadecimal: " + decimal_to_hexadecimal(input_value))
    elif input_type == "2":
        if convert_type == "1":
            print(binary_to_decimal(input_value))
        elif convert_type == "2":
            print(input_value)
        elif convert_type == "3":
            temp = binary_to_decimal(input_value)
            print(decimal_to_hexadecimal(temp))
    elif input_type == "3":
        if convert_type == "1":
            print(hexadecimal_to_decimal(input_value))
        elif convert_type == "2":
            temp = hexadecimal_to_decimal(input_value)
            print(decimal_to_binary(temp))
        elif convert_type == "3":
            print(input_value)

    ##################################### PROGRAM LOOP #################################################

    is_valid = False
    while not is_valid:
        new_conversion = input("Would you like to convert another number/value? (Y/N)\n")
        if new_conversion == "N" or new_conversion == "n":
            is_complete = True
            is_valid = True
        elif new_conversion == "Y" or new_conversion == "y":
            is_valid = True
        else:
            print("INVALID")
