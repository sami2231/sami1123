secret_value = 500

def secretfunction():
    return secret_value

input1 = raw_input("Raw_input():guess the secret number:")


if input1 == secret_value:
    print "you guessed correct"
else:
    print "you guessed wrong"


input2 = input("input(): guess the secret number:")

if input2 == secret_value:
    print "you guessed correct"
else:
    print "you guessed wrong"
