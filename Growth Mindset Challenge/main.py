import random

# List of Growth Mindset Challenges
challenges = [
    "Learn something new about a topic that challenges you.",
    "Turn a mistake into a learning opportunity today.",
    "Give constructive feedback to someone and ask for some in return.",
    "Set a small goal for yourself and accomplish it by the end of the day.",
    "Spend 10 minutes practicing a skill you find difficult.",
    "Read about a successful person who overcame challenges through persistence.",
    "Step out of your comfort zone and try something new today.",
    "Reframe a negative thought into a positive one.",
    "Write down three things you learned this week and how they helped you grow."
]

def get_random_challenge():
    """Returns a random challenge from the list."""
    return random.choice(challenges)

def save_challenge(challenge):
    """Saves the accepted challenge to a file for tracking progress."""
    with open("challenges.txt", "a") as file:
        file.write(challenge + "\n")

def main():
    print("\n🌱 Welcome to the Growth Mindset Challenge! 🌱")
    challenge = get_random_challenge()
    print(f"\n✨ Your challenge for today: \n➡️ {challenge}")

    user_input = input("\nDo you accept this challenge? (yes/no): ").strip().lower()

    if user_input in ["yes", "y"]:
        save_challenge(challenge)
        print("\n✅ Great! Keep growing and challenging yourself! Your progress is saved. 💪")
    else:
        print("\n❌ No worries! Come back tomorrow for a new challenge. 😊")

if __name__ == "__main__":
    main()
