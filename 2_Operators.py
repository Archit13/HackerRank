"""
Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip),
and tax percent (the percentage of the meal price being added as tax) for a meal, find and print the meal's total cost.
"""
meal_cost = float(input())
tip_percent = int(input())
# convert tip to decimal
tip = (round(tip_percent/100, 2)) * meal_cost
tax_percent = int(input())
# convert tax to decimal
tax = (round(tax_percent/100, 2)) * meal_cost
# add cost, tip and tax to get total
total = meal_cost + tip + tax

print("The total cost of the meal is " + str(round(total)) + " dollars.")
