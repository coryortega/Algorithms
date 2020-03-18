#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):

  number_batches = 0
  ingredient_ratios = []

  for i in recipe:
    if i in ingredients == True:
      for j in ingredients:
        if i == j:
          # ingredient_ratios = [(math.floor(ingredients[j] // recipe[i]))]
          ingredient_ratios.append(math.floor(ingredients[j] // recipe[i]))
          # number_batches = math.floor(ingredients[j] // recipe[i])
          return ingredient_ratios

      else:
        return ingredient_ratios.append(0)

  print(ingredient_ratios)
  return ingredient_ratios


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))