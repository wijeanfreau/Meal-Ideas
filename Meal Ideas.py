#This will create a list of dinners and lunches.
import random

dinner = ['Massuman Curry',
          'Loaded Quesadillas',
          'Fettuccine Alfredo',
          'Burgers and Fries',
          'Sweet Pork Burritos',
          'Honey Garlic Stir Fry',
          'Pork Chops with Roasted Mushrooms',
          'Sub Sandwiches',
          'Nasi Goreng',
          'Chicken and Dumplings',
          'Mushroom Soup',
          'Red Sauce Pasta',
          'Mississippi Roast and Mashed Potatoes',
          'Arugala and Pear Salad',
          'Pizza',
          'Chicken Tacos',
          'Pancakes and Bacon',
          'Biscuits and Gravy',
          'Zuppa Tuscana',
          'Grilled Cheese and Tomato Soup',
          'Chili and Cornbread',
          'Steak and Asparagus',
          'Bratwurst',
          'Shawarma Broodjes',
          'Sous Vide Ribs',
          'Pork Chops and Roasted Broccoli',
          'Baked Ziti',
          'Vietnamese Cucumber Salad',
          'Chicken Pot Pie',
          'Adas Polo o Morgh (Chicken with Lentil Rice)',
          'Spaghetti a la Carbonara',
          'Breakfast Burritos',
          'Sloppy Joes',
          'Meatball Subs',
          'Enchiladas',
          'Pad Thai',
          'BLT\'s',
          'Crunchwraps',
          'Shrimp Scampi',
          'Hawaiian Sandwiches',
          'Tomato Jam and Bacon Grilled Cheese',
          'Chicken Rolls',
          'Buffalo Quesadillas with Cucumber Salsa',
          'Quiche',
          'Teriyaki Fried Rice',
          'Dirty Rice',
          'Philly Cheesesteak',
          'Swedish Meatballs and Egg Noodles',
          'Mushroom Pasta',
          'Mustard and Maple Pork',
          'Turkey Sandwiches with Bacon and Red Pepper Jelly'
          ]
lunch = ['Peanut Butter and Jelly Sandwiches',
         'Pre-prepared Burritos'
         ]
breakfast = ['Waffles',
             'Pancakes',
             'Eggs and Bacon'
             ]
print('How many dinner ideas would you like?')
dinput = int(input())
numdin = int(min(dinput, len(dinner)))
print('How many lunch ideas would you like?')
linput = int(input())
numlun = int(min(linput, len(lunch)))
print('How many breakfast ideas would you like?')
binput = int(input())
numbre = int(min(binput, len(breakfast)))

print('Here are your dinner ideas: ')
print(random.sample(dinner, numdin))
print('Here are your lunch ideas: ')
print(random.sample(lunch, numlun))
print('Here are your breakfast ideas: ')
print(random.sample(breakfast, numbre))