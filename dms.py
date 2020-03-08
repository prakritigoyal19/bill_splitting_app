def simplifyDebt(transactions):
    # Simplify Debt Function to simplify Transcation
    paidTo = {}     # Persons with amount paid
    paidFrom = {}   # Persons with amount received

    # Iterate each transaction to assign total paid amount and total received amount of each person
    for transaction in transactions:
        sum = 0
        for person in transaction["paidFor"]:
            sum += transaction["paidFor"][person]
            if person in paidTo:
                paidTo[person] += transaction["paidFor"][person]
            else:
                paidTo[person] = transaction["paidFor"][person]
        if transaction["paidBy"] in paidFrom:
            paidFrom[transaction["paidBy"]] += sum
        else:
            paidFrom[transaction["paidBy"]] = sum

    # normalize paid and received amount of same person
    for person in paidTo:
        if person in paidFrom:
            if paidFrom[person] <= paidTo[person]:
                paidTo[person] -= paidFrom[person]
                # Remove person from list if amount value is 0
                del paidFrom[person]
            else:
                paidFrom[person] -= paidTo[person]
                paidTo[person] = 0

    # normalize received amount and paid amount
    for person in paidFrom:
        if person in paidTo:
            if paidTo[person] <= paidFrom[person]:
                paidFrom[person] -= paidTo[person]
                # Remove person from list amount value is 0
                del paidTo[person] #= 0
            else:
                paidTo[person] -= paidFrom[person]
                paidFrom[person] = 0
    # Return paidFrom and paidTo person's list with remaining amount
    return paidFrom, paidTo


n = int(raw_input("Enter the number of friends: "))
tr = []
for i in range(n):
    t = {}
    t["paidBy"]=raw_input("Enter the name of friend "+ str(i+1) + ": ")
    x = int(raw_input("Enter the number of people that owe "+ t["paidBy"] + ": "))
    l = []
    t["paidFor"]={}
    for j in range(x):
        name=raw_input("Enter the name of person: ");
        l.append(name)
        t["paidFor"][l[j]]=int(raw_input("Enter the amount: "))
    tr.append(t)


"""# test case 1
transactions1 = [{ "paidBy": "D", "paidFor": { "A": 2, } },
{ "paidBy": "A", "paidFor": { "B": 9} }, { "paidBy": "B", "paidFor": { "A": 7, "D": 5}},
{ "paidBy": "C", "paidFor": { "D": 3, "A":10 } }]

# Test Case Example
# If A is paying amount to B and C then one transcation would be
# {"paidBy":"A", "paidFor":{"B":val1, "C":val2}}"""

# Call the function with passing array of transcation


paidFrom, paidTo = simplifyDebt(tr)

# print the personfrom and personTo with amount
for person1 in paidTo:
    for person2 in paidFrom:
        if paidTo[person1] >= paidFrom[person2]:
            # Print person name with its owes to person with amount
            if paidFrom[person2] != 0:
                print person1, "owes ", person2, paidFrom[person2]
                paidTo[person1] -= paidFrom[person2]
                paidFrom[person2] = 0
        else:
            if paidTo[person1] !=0:
                print person1, "owes ", person2, paidTo[person1]
                paidFrom[person2] -= paidTo[person1]
                paidTo[person1] = 0