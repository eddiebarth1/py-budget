# py-budget
Minimal Python-Based Budget App (Command Line to Start)

### What Does it Do?
- Can take a new-line delimited file that lists expenses with a dollar value, lists them in a nice format, and subtracts their total from the paycheck amount. 
  - Particularly useful for recurring expenses that infrequently change, but are ever-present

### To Run: 
Simply run the budgeting.py script!  As of this writing (19-September 2019), it takes two arguments: 

- `-p` for "Paycheck" dollar amount.
- `-f` for "File".  This file 

*Example:* `python Budgeting.py -p 1100 -f sample_expenses`

Sample expense file - new-line delimited as "Expense_name", $Dollar_amount
```
Car Insurance, 55.87
Car Gas, 35
Electricity, 45
Groceries, 150
Hulu, 59.99
Rent, 750

```


### Example Output From Above Example:
```
╭─eddie@eddie-manjaro ~/repos/py-budget  ‹master*› 
╰─➤  python Budgeting.py -p 1100 -f sample_expenses 

Total pay for this period is: $1100.0 

Your expenses for this period are: 

{'Car Gas': 35.0,
 'Car Insurance': 55.87,
 'Electricity': 45.0,
 'Groceries': 150.0,
 'Hulu': 59.99,
 'Rent': 750.0}

 Total bill payments = $1095.86 

Your remaining balance after bills will be: 4.14
```
