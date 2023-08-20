# 🎉 Birthday Greetings 🎈

This code showcases a fantastic way to spread birthday joy! It demonstrates how to display a list of users who deserve a warm birthday greeting in the upcoming week.

## 🚀 Usage

1. **Populate the List of Celebrants**: Open the `main.py` file and fill the `users` list. For each individual, add a dictionary with their name and birthday in the format `datetime.datetime(year, month, day)`.

    ```python
    users = [
        {"name": "Bill", "birthday": datetime.datetime(2000, 8, 16)},
        {"name": "Jill", "birthday": datetime.datetime(1995, 8, 18)},
        # Add more users here
    ]
    ```

2. **Run the Script**: Fire up your terminal and run the following command to unleash birthday magic:

    ```bash
    python main.py
    ```

3. **Witness the Celebration**: The program will illuminate your terminal with a list of individuals deserving a birthday shoutout in the upcoming week. Birthdays falling on weekends will get a special shoutout on Monday.

## 🎁 Example Output

    🎂 Upcoming birthdays 🎉:
    Tuesday: Bill, Jill
    Friday: Kim, Jan


## ⚠️ Important

This code relies on the built-in `datetime` module, eliminating the need for extra installations. Please ensure you accurately provide user data in the `users` list.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
