from matplotlib.pyplot import pyplot as plt
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from numpy import arange
from pandas import DataFrame
Commits:

1. Refactor imports in PersonalFinanceAdvisorySystem class:
```
```

2. Rename variables in generate_recommendations() method:
```
expenses_amounts - -> expenses_amounts_values
expense_indices - -> expenses_indices
```

3. Add error handling for risk_appetite input in generate_investment_advice() method:
```
if risk_appetite.lower() not in ('low', 'medium', 'high'):
    return "Invalid risk appetite input. Please enter 'low', 'medium', or 'high'."
```

4. Add error handling for empty DataFrame in analyze_spending() method:
```
if self.expenses.empty:
    print("No expenses recorded.")
    return
```

5. Encapsulate plotting functionality in analyze_spending() method:
```


def analyze_spending(self):
    if self.expenses.empty:
        print("No expenses recorded.")
        return

    category_expenses = self.expenses.groupby('Category').sum()
    self.plot_spending_analysis(category_expenses)


def plot_spending_analysis(self, category_expenses):
    category_names = category_expenses.index
    amounts = category_expenses['Amount']

    plt.bar(category_names, amounts)
    plt.xlabel('Category')
    plt.ylabel('Amount')
    plt.title('Spending Analysis')
    plt.show()


```

6. Improve formatting of revenue streams in generate_profitability() method:
```python
revenue_streams = [
    {'stream': 'Subscription Model', 'description': '- Offer both a free version with limited features and a premium subscription plan with advanced features and access to specialized financial advice.'},
    {'stream': 'Partnerships', 'description': '- Collaborate with financial institutions or investment platforms to provide referral services, earning commission on investments made through recommendations.'},
    {'stream': 'Data Analysis Services', 'description': '- Offer aggregated and anonymized financial data analysis to financial institutions or market research companies, providing valuable insights and trends.'},
    {'stream': 'Advertising and Partnership Opportunities',
        'description': '- Partner with relevant financial service providers to display targeted ads or offers to users, generating advertising revenue.'},
    {'stream': 'API Integration', 'description': '- Enable third-party developers to integrate the Intelligent Personal Finance Advisory System into their applications through API integration, generating licensing fees.'}
]

return revenue_streams
```
