hypothetical_foods = set('sandwitch','cake','apple','almonds')

food_1 = input()
food_2 = input()
food_3 = input()

user_foods = set(food_1,food_2,food_3)

print('Enter your first favorite food:', food_1)
print('Enter your second favorite food:', food_2)
print('Enter your third favorite food:', food_3)



if hypothetical_foods=user_foods:
    print('Our common food(s):',)
else:
    print('We have no common foods')