import random

class Character:
    def __init__(self, name, role):
        self.name = name
        self.role = role

def get_character_input(role):
    name = input(f"Enter the {role}'s name: ")
    return Character(name, role)

def generate_story():
    main_character = get_character_input("main character")
    sidekick = get_character_input("sidekick")
    villain = get_character_input("villain")

    settings = ["a magical kingdom", "a futuristic city", "an ancient forest", "a hidden cave"]
    chosen_setting = random.choice(settings)

    plot_twist = input("Enter a plot twist for the story: ")

    story = f"Once upon a time, in {chosen_setting}, there lived a {main_character.role} named {main_character.name}. "
    story += f"{main_character.name} was accompanied by a loyal {sidekick.role}, {sidekick.name}, and they were facing their arch-nemesis, {villain.name}.\n\n"

    story += f"One day, while exploring {chosen_setting}, they encountered a surprising twist: {plot_twist}\n\n"

    story += f"{villain.name}: \"Ah, {main_character.name}! Your journey ends here!\"\n"
    story += f"{main_character.name}: \"Not so fast, {villain.name}! With the help of {sidekick.name}, we will overcome this challenge!\"\n\n"

    story += "And so, the epic adventure continued, full of twists and turns, until they reached a surprising conclusion.\n\n"
    story += f"In the end, {main_character.name}, {sidekick.name}, and even {villain.name} learned valuable lessons, and the world of {chosen_setting} was forever changed. The end."

    return story

if __name__ == "__main__":
    story = generate_story()
    print(story)
