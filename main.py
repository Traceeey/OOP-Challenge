Main.py
from pet import Pet

def display_menu():
    print("\nWhat would you like to do?")
    print("1. Feed your pet")
    print("2. Play with your pet")
    print("3. Teach a trick")
    print("4. Put pet to sleep")
    print("5. Show tricks")
    print("6. Check status")
    print("7. Exit")

def main():
    print("Welcome to the Pet Simulator!")
    
    # Get pet name
    while True:
        pet_name = input("What would you like to name your pet? ").strip()
        if pet_name:
            break
        print("Pet name cannot be empty. Please enter a name!")

    pet = Pet(pet_name)
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ").strip()
        
        if choice == "1":
            pet.feed()
        elif choice == "2":
            pet.play()
        elif choice == "3":
            trick = input("What trick would you like to teach? ").strip()
            if trick:
                pet.teach_trick(trick)
            else:
                print("Trick name cannot be empty!")
        elif choice == "4":
            pet.sleep()
        elif choice == "5":
            pet.show_tricks()
        elif choice == "6":
            pet.check_status()
        elif choice == "7":
            print(f"Goodbye! {pet.name} will miss you! 🐾")
            break
        else:
            print("Invalid choice. Please enter a number between 1-7.")

if __name__ == "__main__":
    main()
