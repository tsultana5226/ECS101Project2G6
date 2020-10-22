#Finally, convert your code in Part 3 as a function. The inputs to your function should be L(A1), L(A2), C(A1), and C(A2). The output should be the expected profit. Write a program that explores several different combinations of those four parameters and tries to find the combination that maximizes profit. We are not expecting a program that will always return the best combination, but we want to see at least some thoughtful approach to finding a good combination of values. 


import decimal
import random

# Constants (Costs and Location of the competitors)
LB1 = 4
LB2 = 4
CB1 = 5
CB2 = 5


def max_profit(LA1,LA2,CA1,CA2):    
    Profit = 0
    # For loop conducts 1 million trials
    for i in range (1,1000001):
        # Picks a random number from 0 to 10
        customer_loc=(random.random())*10

        # This function calculates the score based on the location of a store and the price
        def score(location, price):
            return (10 - abs(customer_loc - location) + 3 * (6 - price))

        # Calculates each stores score
        Score_A1= score(LA1,CA1)
        Score_A2= score(LA2,CA2)
        Score_B1= score(LB1,CB1)
        Score_B2= score(LB2,CB2)

        # The sum of each stores score
        total_score= Score_A1 + Score_A2 + Score_B1 + Score_B2