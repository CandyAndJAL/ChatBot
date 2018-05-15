# Insert ChatBot name here with one sentence summary of what is does
'''I will use the bot to try to figure out a meal that would fit your liking.
I’ll ask for the user’s mood and the time of the day, in order to find the food that is right for them at that certain time.
For example, if they are depressed during the night FoodBot will suggest some food that would “cure depression.”
I am still trying to see if I can make it more of a conversation bot as it finds these foods but I don’t really know what 
it will say after it gives the user 4 meal options.'''
import random

bot_template = "BOT: {0}"
user_template = "USER: {0}"

print("What is your name?")
name = raw_input()
FoodBot = ["Hey, I'm FoodBot, ask me for food recommendations for any mood or time.", "Hola, Soy FoodBot"]
print(random.choice(FoodBot))


feeling = input("How are you feeling at the moment? 1)Anxious 2)Happy )Tired")
time = input("WHat time is it? 1)Morning 2)Afternoon 3)Night")

if feeling and time == 1:
  print("Maybe you should try: \n 1. Fortified whole-grain cereal with low-fat milk and blueberries \n 2. Buckwheat pancakes \n 3. Full-fat Greek yogurt with honey and granola \n 4. Salmon salad with vinaigrette")
if feeling == 1 and time == 2:
  print("You may like to consider: \n 1. Vegan Spinach Quiche \n 2. Classic Nut Loaf \n 3. Vegan Ruben Sandwich \n 4. Egg Fried Cauliflower Rice")
if feeling == 1 and time == 3:
  print("You may like to consider: \n 1. Grilled Salmon Burgers with Avocado Salsa \n 2. Skillet Mushroom Chicken and Quinoa \n 3. Black Bean Meatless Balls \n 4. Savory Oatmeal with Garlicky Kale")
if feeling == 2 and time == 1:
  print("You may like to consider: \n 1. Vegan Spinach Quiche \n 2. Classic Nut Loaf \n 3. Vegan Ruben Sandwich \n 4. Egg Fried Cauliflower Rice")
if feeling and time == 2:
  print("Maybe you should try: \n 1. Fortified whole-grain cereal with low-fat milk and blueberries \n 2. Buckwheat pancakes \n 3. Full-fat Greek yogurt with honey and granola \n 4. Salmon salad with vinaigrette")
if feeling == 2 and time == 3:
  print("You may like to consider: \n 1. Grilled Salmon Burgers with Avocado Salsa \n 2. Skillet Mushroom Chicken and Quinoa \n 3. Black Bean Meatless Balls \n 4. Savory Oatmeal with Garlicky Kale")
if feeling == 3 and time == 1:
  print("Oats with ground flax, blueberries, and chopped nuts", "A slice of whole grain toast with avocado and an egg", "Veggie omelet and whole wheat toast or side of fruit")
if feeling == 3 and time == 2:
  print("You may like to consider: \n 1. Vegan Spinach Quiche \n 2. Classic Nut Loaf \n 3. Vegan Ruben Sandwich \n 4. Egg Fried Cauliflower Rice")
if feeling and time == 3:
  print("Maybe you should try: \n 1. Fortified whole-grain cereal with low-fat milk and blueberries \n 2. Buckwheat pancakes \n 3. Full-fat Greek yogurt with honey and granola \n 4. Salmon salad with vinaigrette")
  
