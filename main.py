Main.py
from pet import Pet

def main():
    print("Welcome to the Pet Simulator!")
    pet_name = input("What would you like to name your pet? ")
    pet = Pet(pet_name)
    
    while True:
        print("\nWhat would you like to do?")
        print("1. Feed your pet")
        print("2. Play with your pet")
        print("3. Teach a trick")
        print("4. Put pet to sleep")
        print("5. Show tricks")
        print("6. Check status")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")
        
        if choice == "1":
            pet.feed()
        elif choice == "2":
            pet.play()
        elif choice == "3":
            trick = input("What trick would you like to teach? ")
            pet.teach_trick(trick)
        elif choice == "4":
            pet.sleep()
        elif choice == "5":
            pet.show_tricks()
        elif choice == "6":
            pet.check_status()
        elif choice == "7":
            print(f"Goodbye! {pet.name} will miss you!")
            break
        else:
            print("Invalid choice. Please enter a number between 1-7.")
        
        # Simulate time passing after each action
        pet.time_passes()

if _name_ == "_main_":
    main()
