#!/usr/bin/python

import argparse

def find_max_profit(prices):
  #create variable to store max profit
  #TEMPORARILY set it to -100, meaning this algo won't work if we have a profit loss less than -100
  max_profit = -100

  #'i' is iterating through each price, EXCLUDING the last element
  for i in range(len(prices)-1):
    #'j' is iterating through every price AFTER 'i'
    for j in range(i+1, len(prices)):
      # 'j' is being subtracted from 'i', and if they result in a number greater than 'max_profit' then...
      if prices[j] - prices[i] > max_profit:
        # ...'max_profit' is now reasigned to the largest number
        max_profit = prices[j] - prices[i]
  
  return max_profit


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line.
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))