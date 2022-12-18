# Expense Tracker 💸
The `expense-tracker` app lets you manage your expense by tracking them for you. Also, it is possible to `budget` your expenditure so that you don't spend more than you need to.

## Features
---
### Add expense
With a button click ➕ a simple UI can help you record an expense with the app. The expenditure will then appear on the list of expenses on the home screen. You can add spending with a proper `category`, `date`, and `amount`.

### View Expenses
On the home screen, you will see all your recorded expenses in one place with the flexibility to `edit` ✎ and change them.

### Set Budget
It is possible to set a cap on the expenditure for the `budget cycle`. You can fix an overall budget in a selected currency. As the expenses get recorded, your budget will show how much money is left to spend in the current cycle. 

### Category chart
On the budget page, a `donut chart` shows the categories in which you are spending your money. The category of expense can help you understand the type of expense you have the most. 

### Settings
- The set `currency` can be changed easily on the settings page. By default, the currency will be USD.  
- You have the flexibility to start your budget cycle from any day of the month. The `reset day` set out a day on which you want to start your budget(maybe your salary day 😉). By default, it is set to the first of every month.

### Profile
In the profile section, you can see your current email and username. You can also `change password` if required. 

# Project design
## Tech stack
- Python with Django framework in the backend.
- HTML, CSS, and JS for the front end.
- SQLite for the Database.
- CharJs for graphs.
## Project structure
```
├── capstone
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── expense_tracker
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── static
│   │   ├── budget.js
│   │   ├── expense.js
│   │   └── styles.css
│   ├── templates
│   │   ├── add_expense.html
│   │   ├── budget.html
│   │   ├── index.html
│   │   ├── layout.html
│   │   ├── login.html
│   │   ├── profile.html
│   │   ├── register.html
│   │   ├── set_budget.html
│   │   └── settings.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── manage.py
└── requirements.txt
```
## File details
### models
- models.py file contains definitions of the models `(User, Settings, Budget, Category, and Expense)`, that represent the data structures used in the application. I am using these models to store and retrieve information from the database.

### static
_ The `expense.js` and `budget.js` files have logic for their respective javascript logic to make `Ajax API calls` to the backend and to construct the `donut chart`.
- `style.css` file is there to add some custom CSS.

### templates
- All the views have their respective jinja templates. For instance, `budget.html` for the budget view, `profile.html` for the profile view, and so on.

### urls.py
- urls.py file defines the patterns for URLs that the app will accept. These patterns determine which view functions to call when a user accesses an endpoint.
- It also helps to decouple the URLs from the app from the underlying view functions, which can make it easier to make changes to the app in the future.

### views.py
- The view.py consist of all the route handler functions. The handler functions do all kind of database queries, request and response handling, and business logic. 


## How to run
### Install packages
``` 
    pip3 install -r requirements.txt
```
### To make migrations
```
python3 manage.py makemigrations
```
### To apply migrations
```
python3 manage.py migrate
```

### To run the application
```
python3 manage.py runserver
```

## Distinctiveness and complexity 
This project is a final project for the CS50 web course. 
- The project is entirely different from what I have built for this course thus far. 
- This project can have many more features from what it has now. It was particularly complex in-terms of the `initial design` and `UX` of expense tracking along with a budget cap.
- Providing the features like `reset day` for a flexible budget cycle brought a little bit of complexity in the backend logic side.
- Few more things that brought some more complexity were:
  - Change password.
  - Chart implementation. 
  - Mobile responsiveness. 


