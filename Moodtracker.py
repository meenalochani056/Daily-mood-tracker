import datetime

def save_mood(mood):
    today = datetime.date.today()
    with open("mood_log.txt", "a") as file:
        file.write(f"{today}: {mood}\n")
    print("✅ Mood saved!")

def view_history():
    try:
        with open("mood_log.txt", "r") as file:
            logs = file.readlines()
            print("\n📅 Mood History:")
            for line in logs:
                print(line.strip())
    except FileNotFoundError:
        print("No mood history found!")

def mood_summary():
    try:
        with open("mood_log.txt", "r") as file:
            logs = file.readlines()
            summary = {}
            for line in logs:
                mood = line.strip().split(": ")[-1]
                summary[mood] = summary.get(mood, 0
