print("1. Write Note")
print("2. Read Notes")

choice = input("Enter your choice (1/2): ")

if choice == "1":
    note = input("Enter your notes: ")
    with open("notes.txt", "a") as f:
        f.write(note + "\n")
    print("Notes saved!")

elif choice == "2":
    try:
        with open("notes.txt", "r") as f:
            content = f.read()
            print("\nYour Notes:")
            print(content)
    except FileNotFoundError:
        print("No Notes Found!")

else:
    print("Invalid Choice")