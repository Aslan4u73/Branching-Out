import json


def load_users(path="users.json"):
    with open(path, "r") as file:
        return json.load(file)


def print_users(users):
    for user in users:
        print(user)


def filter_users_by_name(users, name):
    name = name.lower()
    return [user for user in users if user["name"].lower() == name]


def filter_by_age(users, age):
    return [user for user in users if user["age"] == age]


def filter_by_email(users, email):
    email = email.lower()
    return [user for user in users if user["email"].lower() == email]


def main():
    users = load_users()

    filter_option = input(
        "What would you like to filter by? (Supported: 'name', 'age', 'email'): "
    ).strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        print_users(filter_users_by_name(users, name_to_search))

    elif filter_option == "age":
        age_input = input("Enter an age to filter users: ").strip()
        try:
            age_to_search = int(age_input)
        except ValueError:
            print("Please enter a valid number for age.")
            return
        print_users(filter_by_age(users, age_to_search))

    elif filter_option == "email":
        email_to_search = input("Enter an email to filter users: ").strip()
        print_users(filter_by_email(users, email_to_search))

    else:
        print("Filtering by that option is not yet supported.")


if __name__ == "__main__":
    main()
