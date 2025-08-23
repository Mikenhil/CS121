first_name_input = input('What is your first name: ')
last_name_input = input('What is your last name: ')

age_input = input('Enter your age: ')

def isInteger(num_input):
    try:
        int(num_input)
        return True
    except:
        return False

while (not isInteger(age_input)):
    age_input = input('Age must be a number. Enter your age: ')

print(f'You are {first_name_input} {last_name_input} and you are {age_input}')
