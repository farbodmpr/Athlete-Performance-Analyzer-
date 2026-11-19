# Athlete Performance Analyzer

# Store all athlete information
athletes = []

# Store athlete names
athlete_names = []

# Store all performance averages
all_averages = []

# Register 5 athletes
for i in range(5):

    print("\n========== ATHLETE", i + 1, "==========")

    name = input("Enter athlete name: ").strip().capitalize()

    if name == "":
        print("Name cannot be empty.")
        continue

    sport = input("Enter sport name: ").strip().capitalize()

    if sport == "":
        print("Sport name cannot be empty.")
        continue

    weight = input("Enter athlete weight in kg: ").strip()

    if weight.isdigit() is False:
        print("Invalid weight.")
        continue

    weight = float(weight)

    if weight <= 0:
        print("Weight must be greater than zero.")
        continue

    # Store 3 performance records
    records = []

    for j in range(3):

        record = input("Enter performance score (0-100): ").strip()

        if record.isdigit() is False:
            print("Invalid score.")
            continue

        record = float(record)

        if record < 0 or record > 100:
            print("Score must be between 0 and 100.")
            continue

        records.append(record)

    # Register athlete only if all records are valid
    if len(records) == 3:

        athletes.append([name, sport, weight, records])
        athlete_names.append(name)

    else:
        print("Athlete registration was incomplete.")

# Analyze athlete performance
print("\n========== ATHLETE REPORT ==========")

total_average = 0

if len(athletes) > 0:

    for athlete in athletes:

        name = athlete[0]
        sport = athlete[1]
        weight = athlete[2]
        records = athlete[3]

        total = 0

        for record in records:
            total += record

        average = total / len(records)

        total_average += average
        all_averages.append(average)

        print("\nName:", name)
        print("Sport:", sport)
        print("Weight:", weight, "kg")
        print("Records:", records)
        print("Average Performance:", average)

        # Determine athlete performance level
        if average >= 90:
            print("Level: Excellent")

        elif average >= 75:
            print("Level: Good")

        elif average >= 50:
            print("Level: Average")

        else:
            print("Level: Needs Improvement")

    # Calculate overall average
    overall_average = total_average / len(athletes)

    print("\n========== GENERAL REPORT ==========")
    print("Number of Athletes:", len(athletes))
    print("Overall Performance Average:", overall_average)

    # Find the best and weakest athletes
    best_athlete = athletes[0]
    weakest_athlete = athletes[0]

    for athlete in athletes:

        total = 0

        for record in athlete[3]:
            total += record

        average = total / len(athlete[3])

        best_total = 0

        for record in best_athlete[3]:
            best_total += record

        best_average = best_total / len(best_athlete[3])

        weakest_total = 0

        for record in weakest_athlete[3]:
            weakest_total += record

        weakest_average = weakest_total / len(weakest_athlete[3])

        if average > best_average:
            best_athlete = athlete

        if average < weakest_average:
            weakest_athlete = athlete

    print("\nBest Athlete:", best_athlete[0])
    print("Sport:", best_athlete[1])

    print("\nWeakest Athlete:", weakest_athlete[0])
    print("Sport:", weakest_athlete[1])

    # Sort athlete names alphabetically
    athlete_names.sort()

    print("\n========== ATHLETE LIST ==========")

    for name in athlete_names:
        print(name)

    # Search for an athlete
    search_name = input("\nEnter athlete name to search: ").strip().lower()

    found = False

    for athlete in athletes:

        if search_name in athlete[0].lower():

            print("\nAthlete Found:", athlete[0])
            print("Sport:", athlete[1])
            print("Weight:", athlete[2])
            print("Records:", athlete[3])

            found = True
            break

    else:
        print("Athlete not found.")

else:
    print("No valid athletes were registered.")

print("\nProgram finished.")
