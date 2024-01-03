def words_to_digits(phone_number):
    # Create a dictionary to map words to digits.
    word_to_digit = {
        'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
        'six': '6', 'seven': '7', 'eight': '8', 'nine': '9', 'zero': '0'
    }

    # Split the input string into words.
    words = phone_number.split()

    # Initialize variables to store the result and handle repeated digits.
    result = []
    current_digit = ''
    digit_count = 0
    cnt=1

    for word in words:
        if word in word_to_digit:
            digit = word_to_digit[word]
            if digit == current_digit:
                digit_count += 1
                if digit_count == 2:
                    result.append('')
                elif digit_count == 3:
                    result.pop()  # Remove the previous 'double'
                    result.append('')
                # For four or more repetitions, use 'double' and 'triple' multiple times (e.g., "double double two" => "2222").
                elif digit_count > 3:
                    result.append('' * (digit_count - 1))
                # Append the digit once.
                result.append(digit*cnt)
                cnt = 1
            else:
                current_digit = digit
                digit_count = 1
                result.append(digit*cnt)
                cnt = 1
        elif word == 'double' :
            cnt=2
        else : 
            cnt = 3

    # Join the result list to obtain the final phone number in digits.
    return ''.join(result)

phone_number_words = input("enter the digits in alphabets")
phone_number_digits = words_to_digits(phone_number_words)
print(phone_number_digits)  