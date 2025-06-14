class Category:
    def __init__(self, category):
        self.ledger = []
        self.category = category

    def __str__(self):
        info = f'{self.category.center(30, "*")}'
        for operation in self.ledger:
            description = operation['description'][:23]
            amount = str("{:.2f}".format(operation['amount']))
            spaces = 30 - len(description) - len(amount)
            line = description + ' ' * spaces + amount
            info += f'\n{line}'
        total = f"\nTotal: {self.get_balance():.2f}"
        info += total
        return info

    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -(amount), 'description': description})
            return True
        else:
            return False

    def get_balance(self):
        return sum(op['amount'] for op in self.ledger)
    
    def transfer(self, amount, other_category): 
        #other_category is an object
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {other_category.category}')
            other_category.deposit(amount, f'Transfer from {self.category}')
            return True
        else:
            return False

    def check_funds(self, amount):
        if self.get_balance() >= amount:
            return True
        else:
            return False

def create_spend_chart(categories):
    
    category_spends = [sum(abs(op['amount']) for op in c.ledger if op['amount'] < 0) for c in categories]
    total_spends = sum(category_spends)
    percentages = [int((spend / total_spends) * 100 // 10) * 10 for spend in category_spends]

    chart_lines = [ f"\n{str(i).rjust(3)}| " + ''.join('o  ' if p >= i else '   ' for p in percentages) for i in range(100, -1, -10) ]   
    
    divisor = f"\n    {'-' * (len(categories) * 3 + 1)}"
                   
    largest_name = max(len(c.category) for c in categories)

    names = [c.category.ljust(largest_name) for c in categories]
    name_lines = ['     ' + '  '.join(row) + '  ' for row in zip(*names)]

    return 'Percentage spent by category' + ''.join(chart_lines) + divisor + '\n' + '\n'.join(name_lines)

food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)
print(create_spend_chart([food, clothing]))