from pet import Pet
import random

pet_emojis = {
    "dog": "🐶",
    "cat": "🐱",
    "dragon": "🐉",
    "bunny": "🐰",
    "fox": "🦊",
    "unicorn": "🦄"
}

custom_actions = {
    "dog": "chased its tail and got dizzy 🌀",
    "cat": "knocked a cup off the table 😼",
    "dragon": "breathed fire into the sky 🔥",
    "bunny": "hopped around happily 🐇",
    "fox": "did a sneaky spin 🌀",
    "unicorn": "sprinkled glitter everywhere ✨"
}

def print_menu():
    print("\nWhat would you like to do?")
    print("1. Eat 🍖")
    print("2. Sleep 😴")
    print("3. Play 🎾")
    print("4. Train a new trick 🧠")
    print("5. Show learned tricks 🎓")
    print("6. Do something fun! 🎉")
    print("7. Check pet status 📊")
    print("8. Quit ❌")

def main():
    # Choose a pet type
    print("Welcome! Choose your pet type:")
    for pet in pet_emojis:
        print(f"- {pet.title()} {pet_emojis[pet]}")

    pet_type = input("Enter pet type: ").strip().lower()
    if pet_type not in pet_emojis:
        print("Unknown type, we'll make it a mysterious creature 👾")
        pet_type = "creature"
        emoji = "👾"
    else:
        emoji = pet_emojis[pet_type]

    # Name your pet
    pet_name = input(f"What would you like to name your {pet_type} {emoji}? ")
    my_pet = Pet(pet_name)

    greetings = [
        f"{pet_name} rolls over excitedly to greet you!",
        f"{pet_name} gives you a happy little jump!",
        f"{pet_name} is so excited to hang out with you!",
        f"{pet_name} lets out a joyful sound!"
    ]

    print(f"\n🎉 {random.choice(greetings)} Let's play with your {pet_type} {emoji}!\n")

    while True:
        print_menu()
        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            my_pet.eat()
        elif choice == '2':
            my_pet.sleep()
        elif choice == '3':
            my_pet.play()
        elif choice == '4':
            trick = input("Enter a new trick to teach your pet: ")
            my_pet.train(trick)
        elif choice == '5':
            my_pet.show_tricks()
        elif choice == '6':
            action = custom_actions.get(pet_type, f"{pet_name} spins in a circle!")
            print(f"{emoji} {pet_name} {action}")
            my_pet.happiness = min(10, my_pet.happiness + 1)
        elif choice == '7':
            mood = "😢 Sad" if my_pet.happiness <= 3 else "😐 Okay" if my_pet.happiness <= 6 else "😄 Happy"
            print(f"Current mood: {mood}")
            my_pet.get_status()
        elif choice == '8':
            print(f"Goodbye! {pet_name} {emoji} will miss you! 💕")
            break
        else:
            print("Invalid choice, please pick a number between 1 and 8.")

if __name__ == "__main__":
    main()
