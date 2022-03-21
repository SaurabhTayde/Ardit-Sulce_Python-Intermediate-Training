
#    print("Hi %s, you have %s years of experience." % (name, experience_years))

#statement1 = input('Say somthing: ')
#statement2 = input('Say somthing: ')
#statement3 = input('Say somthing: ')

#while True:
#    statement4 = input('Say somthing: ')
#    if statement4 == '\end':
#        break
#    else:
#        continue

# Write a code that takes multiple sentences from user,(code stops taking sentences if '\end' is given by the user)
# capitalize first letter of every sentence
# interprets it whether it's question or statement.
# Combine these sentences with either question mark or full stop depending upon sentence given by user.

# Solution:

def sentence_maker(phrase):
    interrogatives = ('When', 'What', 'How', 'Where', 'Why')
    capitalized = phrase.capitalize()
    if capitalized.startswith(interrogatives):
        return '{}?'.format(capitalized)
    else:
        return '{}.'.format(capitalized)
    
results = []

while True:
    user_input = input('Say Something: ')
    if user_input == '\end':
        break
    else:
        results.append(sentence_maker(user_input))

print(' '.join(results))
