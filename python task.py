def mood_tracker():
    print("Welcome to the Mood Tracker!")
    print("Please choose your mood from the following options:")
    print("1. Happy")
    print("2. Sad")
    print("3. Stressed")
    print("4. Relaxed")
    print("5. Energetic")
    
    allowed_moods = {
        "1": "happy",
        "2": "sad",
        "3": "stressed",
        "4": "relaxed",
        "5": "energetic",
        "happy": "happy",
        "sad": "sad",
        "stressed": "stressed",
        "relaxed": "relaxed",
        "energetic": "energetic"
    }
    
    days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    mood_log = []

    # Collect mood input for each day
    for day in days_of_week:
        while True:
            mood_input = input(f"How do you feel on {day}? ").strip().lower()
            if mood_input in allowed_moods:
                mood_log.append(allowed_moods[mood_input].capitalize())
                break
            else:
                print("Invalid input. Please choose a number (1-5) or a word from the options: happy, sad, stressed, relaxed, energetic.")
    
    # Count occurrences of each mood
    mood_counts = {mood.capitalize(): 0 for mood in allowed_moods.values() if mood in allowed_moods.values()}
    for mood in mood_log:
        mood_counts[mood] += 1

    # Calculate percentages
    print("\nMood Breakdown for the Week:")
    total_days = len(days_of_week)
    for mood, count in mood_counts.items():
        percentage = (count / total_days) * 100
        print(f"{mood}: {percentage:.2f}%")
    
    print("\nThank you for using the Mood Tracker!")

# Run the Mood Tracker
mood_tracker()