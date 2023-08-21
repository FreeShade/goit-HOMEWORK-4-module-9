def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError):
            return "Invalid input. Please try again."

    return wrapper


contacts = {}


@input_error
def add_contact(name, phone):
    contacts[name] = phone
    return f"Contact {name} with phone {phone} added."


@input_error
def change_phone(name, phone):
    if name in contacts:
        contacts[name] = phone
        return f"Phone number for {name} updated to {phone}."
    else:
        return f"Contact {name} not found."


@input_error
def get_phone(name):
    if name in contacts:
        return f"Phone number for {name}: {contacts[name]}"
    else:
        return f"Contact {name} not found."


def show_all_contacts():
    if contacts:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    else:
        return "No contacts found."


def main():
    print("Hello! How can I help you?")
    while True:
        command = input().lower().strip()

        if command == "good bye" or command == "close" or command == "exit":
            print("Good bye!")
            break
        elif command == "show all":
            print(show_all_contacts())
        elif command.startswith("add"):
            _, name, phone = command.split(maxsplit=3)
            print(add_contact(name, phone))
        elif command.startswith("change"):
            _, name, phone = command.split(maxsplit=3)
            print(change_phone(name, phone))
        elif command.startswith("phone"):
            _, name = command.split(maxsplit=2)
            print(get_phone(name))
        else:
            print("Unknown command. Please try again.")


if __name__ == "__main__":
    main()
