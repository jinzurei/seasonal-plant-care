import datetime, random
from main import load_plants, search_plants, normalize, get_current_season

# 📅 Test seasonal logic across year
def test_get_current_season():
    assert get_current_season(datetime.date(2025, 3, 21)) == "Spring"
    assert get_current_season(datetime.date(2025, 6, 15)) == "Summer"
    assert get_current_season(datetime.date(2025, 10, 1)) == "Fall"
    assert get_current_season(datetime.date(2025, 12, 25)) == "Winter"
    assert get_current_season(datetime.date(2025, 1, 5)) == "Winter"

# 🔍 Test flexible, real-world searching
import random

def test_search_plants():
    plants = load_plants("plants.csv")

    # Pick a random plant with traits
    eligible = [p for p in plants if p.get("Traits") and len(p["Traits"].strip()) > 3]
    sample = random.choice(eligible)
    
    name_query = sample["Name"]
    trait_fragment = sample["Traits"].split(",")[0].strip()
    nonsense_query = "completelymadeuptrait123"

    print(f"\n🌿 Target Plant: {name_query}")
    print(f"🔎 Trait used for search: '{trait_fragment}'\n")

    # 1. Name-based search
    print("📘 Name Search:")
    results_by_name = search_plants(plants, name_query)
    print(f"🔢 Results found: {len(results_by_name)}")
    assert any(normalize(p["Name"]) == normalize(name_query) for p in results_by_name), f"❌ Expected match for name '{name_query}'"
    print("✅ Name match test passed\n")

    # 2. Trait fragment search
    print("🌿 Trait Fragment Search:")
    results_by_trait = search_plants(plants, trait_fragment)
    print(f"🔢 Results found: {len(results_by_trait)}")
    assert any(normalize(p["Name"]) == normalize(sample["Name"]) for p in results_by_trait), f"❌ Expected trait match for '{trait_fragment}'"
    print("✅ Trait fragment match test passed\n")

    # 3. Nonsense query
    print("🧪 Nonsense Search:")
    results_garbage = search_plants(plants, nonsense_query)
    print(f"🔢 Results found: {len(results_garbage)}")
    assert results_garbage == [], f"❌ Nonsense query '{nonsense_query}' should return no results"
    print("✅ Nonsense test passed 🎉\n")