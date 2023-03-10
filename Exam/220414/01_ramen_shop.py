from collections import deque

bowls_of_ramen = deque(int(x) for x in input().split(", "))
customers = deque(int(x) for x in input().split(", "))


while bowls_of_ramen and customers:
    bowl = bowls_of_ramen.pop()
    customer = customers.popleft()

    if bowl > customer:
        bowl -= customer
        bowls_of_ramen.append(bowl)

    elif bowl < customer:
        customer -= bowl
        customers.appendleft(customer)

if not customers:
    print('Great job! You served all the customers.')
    if bowls_of_ramen:
        print(f'Bowls of ramen left: {", ".join(str(x) for x in bowls_of_ramen)}')
else:
    print(f'Out of ramen! You didn\'t manage to serve all customers.')
    if customers:
        print(f'Customers left: {", ".join(str(x) for x in customers) }')
