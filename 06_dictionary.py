# 06_dictionary.py
friends = ["Ashish", "Rahul", "Aman", "Sneha", "Pooja"]
tuples = [(name, len(name)) for name in friends]
print(tuples)

your_expenses = {"Hotel":1200,"Food":800,"Transport":500,"Attractions":300,"Misc":200}
partner_expenses = {"Hotel":1000,"Food":900,"Transport":600,"Attractions":400,"Misc":150}

your_total = sum(your_expenses.values())
partner_total = sum(partner_expenses.values())

print("Your total:", your_total)
print("Partner total:", partner_total)

if your_total > partner_total:
    print("You spent more")
else:
    print("Partner spent more")

for key in your_expenses:
    diff = abs(your_expenses[key] - partner_expenses[key])
    print(key, "difference:", diff)
