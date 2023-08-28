def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError):
            return "Invalid input. Please try again."

    return wrapper


contacts = {}


def command_handler(command):
    def decorator(func):
        def wrapper(*args):
            return func(*args)

        if command in ["hello", "show all"]:
            return input_error(wrapper)
        elif command in ["add", "change", "phone"]:
            return input_error(wrapper)
        return wrapper

    return decorator


@command_handler("add")
def add_contact(name, phone):
    if name in contacts:
        return f"Contact {name} already exists. Use 'change' command to update the phone number."
    else:
        contacts[name] = phone
        return f"Contact {name} with phone {phone} added."


@command_handler("change")
def change_phone(name, phone):
    if name in contacts:
        contacts[name] = phone
        return f"Phone number for {name} updated to {phone}."
    else:
        return f"Contact {name} not found."


@command_handler("phone")
def get_phone(name):
    if name in contacts:
        return f"Phone number for {name}: {contacts[name]}"
    else:
        return f"Contact {name} not found."


@command_handler("show all")
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
        elif command == "hello":
            print("How can I help you?")
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
