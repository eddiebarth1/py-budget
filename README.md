# py-budget
Minimal Python-Based Budget App (Command Line to Start)

### What Does it Do?
- Can take a new-line delimited file that lists expenses with a dollar value, lists them in a nice format, and subtracts their total from the paycheck amount. 
  - Particularly useful for recurring expenses that infrequently change, but are ever-present

### To Run: 
Simply run the budgeting.py script!  As of this writing (19-September 2019), it takes two arguments: 

- `-p` for "Paycheck" dollar amount.
- `-f` for "File".  This file 

*Example:* `python Budgeting.py -p 3500 -f expense_15th`

Sample expense file - new-line delimited as "Expense_name", $Dollar_amount
```
Car Insurance, 55.87
Car Gas, 35
Electricity, 45
Groceries, 150
Hulu, 59.99
Rent, 750

```
