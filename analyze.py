expenses = [
    {"category": "food", "amount": 120.5},
    {"category": "transport", "amount": 55.3},
    {"category": "food", "amount": 80.2},
    {"category": "entertainment", "amount": 200},
    {"category": "transport", "amount": 45.1}
]

def analyze_expenses(expenses):
    total_sum = 0  
    category_sums = {}  
    
    
    for expense in expenses:
        category = expense['category']
        amount = expense['amount']
        
        
        total_sum += amount
        
        
        if category in category_sums:
            category_sums[category] += amount
        else:
            category_sums[category] = amount
    
    
    max_category = max(category_sums, key=category_sums.get)
    
    return f"Total: {total_sum} Max category: {max_category}"


result = analyze_expenses(expenses)
print(result)
