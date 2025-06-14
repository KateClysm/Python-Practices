class Category:
    def __init__(self, category):
        self.ledger = []
        self.category = category

    def __str__(self):
        info = f'{self.category.center(30, '*')}'
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
        return sum(item['amount'] for item in self.ledger)
    
    def transfer(self, amount, other_category): 
        #other_category is an object
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {other_category.category}')
            other_category.deposit(amount, f'Transfer from {self.category}')
            return True
        else:
            return False

    def check_funds(self, amount):
        if self.get_balance() > amount:
            return True
        else:
            return False

def create_spend_chart(categories):
    category_spends = []
    percentages = []
    
    for category in categories: #list of objects
        spend = 0
        for operation in category.ledger:
            if operation['amount'] < 0:
                spend += abs(operation['amount'])
        category_spends.append(spend)
    total_spends = sum(category_spends)
    for num in category_spends:
        percentages.append(int((num/total_spends) * 100 // 10) * 10)

    chart = 'Percentage spent by category'
    chart_lines = []
    for line in range(100, -1, -10):
        formated_line = f"\n{str(line).rjust(3)}| "
        for category in percentages:
            if category >= line:
                formated_line += 'o  '
            else:
                formated_line += '   '
        chart_lines.append(formated_line)

    divisor = f'\n{5 * " "}{"-" * (3*len(categories))}'

    largest_name = max(len(c.category) for c in categories)

    name_lines = []
    for i in range(largest_name):
        line = '     '
        for c in categories:
            if i < len(c.category):
                line += c.category[i] + '  '
            else:
                line += '   '
        name_lines.append(line)

    chart += ''.join(chart_lines)
    chart += ''.join(divisor)
    chart += '\n'
    chart += '\n'.join(name_lines)

    return chart

food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)

print(create_spend_chart([food, clothing]))