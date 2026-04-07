files = []

def add_file():
    name = input("Enter file name: ")
    size = input("Enter file size: ")
    file_type = input("Enter file type: ")

    if not name or not size or not file_type:
        print("Error: Missing fields")
        return

    # Duplicate check
    for file in files:
        if file["name"] == name and file["size"] == size:
            print("Duplicate file found!")
            return

    file_data = {
        "name": name,
        "size": size,
        "type": file_type
    }

    files.append(file_data)
    print("File added successfully!")


def view_files():
    if not files:
        print("No files stored.")
        return

    for i, file in enumerate(files, 1):
        print(f"{i}. Name: {file['name']}, Size: {file['size']}, Type: {file['type']}")


def menu():
    while True:
        print("\n1. Add File")
        print("2. View Files")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            add_file()
        elif choice == '2':
            view_files()
        elif choice == '3':
            break
        else:
            print("Invalid choice")


menu()