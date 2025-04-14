import csv
import datetime
import re

# 🌿 Load the plant catalog
def load_plants(filename):
    with open(filename, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)

# 🍁 Determine current season
def get_current_season(date=None):
    if date is None:
        date = datetime.date.today()
    month = date.month
    if month in [3, 4, 5]:
        return "Spring"
    elif month in [6, 7, 8]:
        return "Summer"
    elif month in [9, 10, 11]:
        return "Fall"
    else:
        return "Winter"

# 🔍 Normalize input for human-friendly matching
def normalize(text):
    return re.sub(r"[^\w\s]", "", text.lower().strip())

# 🔍 Search with forgiving input (partial, trait, or name)
def search_plants(plants, query):
    words = normalize(query).split()
    results = []

    for plant in plants:
        fields = f"{plant['Name']} {plant['Category']} {plant['Traits']}"
        normalized_fields = normalize(fields)

        if any(word in normalized_fields for word in words):
            results.append(plant)

    return results

# 🪴 Display formatted care info
def display_plant_summary(plant, season):
    print(f"\n🪴 Plant Care Summary: {plant['Name']}")
    print("-" * 34)
    print(f"Category      : {plant['Category']}")
    print(f"Water Needs   : {plant['WaterNeeds']}")
    print(f"Light Needs   : {plant['LightNeeds']}\n")
    
    print(f"📅 Seasonal Care Tips ({season}):")
    print(f"- {plant[season + 'Care']}\n")
    
    print("💡 Advice:")
    print(plant["Advice"])
    print()

# 🎛️ Main program loop
def main():
    plants = load_plants("plants.csv")
    today = datetime.date.today()
    season = get_current_season(today)

    print("\n🌿 Seasonal Plant Care Assistant 🌿")
    print("----------------------------------")
    print(f"Today's Date: {today.strftime('%B %d, %Y')}")
    print(f"Season: {season} (based on the month)\n")

    while True:
        print("What would you like to do?")
        print("1. 🔍 Search plants by name, category, or trait")
        print("2. 🪴  View care guide by exact plant name")
        print("3. Exit\n")
        choice = input("> ").strip()
        if not choice.isdigit():
            print("Invalid option. Please choose 1, 2, or 3.\n")
            continue

        if choice == "1":
            query = input("\nEnter plant name or trait (e.g., 'succulent', 'low light'): ").strip()
            results = search_plants(plants, query)

            if results:
                print(f"\n🔍 Found {len(results)} result(s):\n")
                for idx, plant in enumerate(results, 1):
                    print(f"[{idx}] 🌱 {plant['Name']}")
                    print(f"    🏷️  Category   : {plant['Category']}")
                    print(f"    💧 Water Needs: {plant['WaterNeeds']}")
                    print(f"    ☀️  Light Needs: {plant['LightNeeds']}")
                    print(f"    🧬 Traits     : {plant['Traits']}\n")
        
                try:
                    index = int(input("Type the number of the plant you want to view (or 0 to cancel): ").strip())
                    if 1 <= index <= len(results):
                        display_plant_summary(results[index - 1], season)
                    elif index == 0:
                        print()
                    else:
                        print("Invalid selection.\n")
                except ValueError:
                    print("Invalid input. Please enter a number.\n")

            else:
                print("No matching plants found.\n")

        elif choice == "2":
            name = input("\nEnter the full name of the plant: ").strip().lower()
            matches = [p for p in plants if normalize(p["Name"]) == normalize(name)]
            if matches:
                display_plant_summary(matches[0], season)
            else:
                print("Plant not found.\n")

        elif choice == "3":
            print("\nGoodbye 🌱")
            break
        else:
            print("Invalid option. Please choose 1, 2, or 3.\n")

if __name__ == "__main__":
    main()