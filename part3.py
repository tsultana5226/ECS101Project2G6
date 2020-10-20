import random

LA1=4
LA2=4
LB1=4
LB2=4
CA1=4
CA2=4
CB1=5
CB2=5
Profit=0

for i in range (1,1000001):

    customer_loc=(random.random())*10

    def score(location,price):
        return (10-abs(customer_loc-location)+3*(6-price))

    Score_A1= score(LA1,CA1)
    Score_A2= score(LA2,CA2)
    Score_B1= score(LB1,CB1)
    Score_B2= score(LB2,CB2)

    total_score= Score_A1 + Score_A2 + Score_B1 + Score_B2
    
    Prob_A1= Score_A1/total_score
    Prob_A2= Score_A2/total_score
    Prob_B1= Score_B1/total_score
    Prob_B2= Score_B2/total_score

    Customer_Pick = random.random()

    if Customer_Pick<Prob_A1:
        Store = "A1"
        Profit = Profit + (CA1-2)

