import random

# Inputs for program
LA1 = 4
LA2 = 4
LB1 = 4
LB2 = 4
CA1 = 4
CA2 = 4
CB1 = 5
CB2 = 5
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

    # Finds the customer's probability of each store by doing the stores score divided by the total score
    Prob_A1= Score_A1/total_score
    Prob_A2= Score_A2/total_score
    Prob_B1= Score_B1/total_score
    Prob_B2= Score_B2/total_score

    # Picks a number from 0 to 1
    Customer_Pick = random.random()

    # This block of code checks which probability range that the customer falls in and pics the proper store accordingly
    if Customer_Pick<Prob_A1:
        Store = "A1"
        Profit = Profit + (CA1-2)
    elif Customer_Pick < (Prob_A1 + Prob_A2):
        Store = "A2"
        Profit = Profit + (CA2 - 2)
    elif Customer_Pick < (Prob_A1 + Prob_A2 + Prob_B1):
        Store = "B1"
    else:
        Store = "B2"

# This line calculates the average profit by divided by 1 million which is the number of trials and prints the output
Avg_Profit = Profit / 1000000
print(Avg_Profit)

