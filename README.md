# 🌿 Seasonal Plant Care Assistant - Final Project Summary
**Jin**  
BYU–Idaho | CSE 111: Programming with Functions  
Week 07 - Student Chosen Project

---

## 🌟 Overview
This is a user-focused, interactive terminal program designed to help users care for houseplants using natural language queries. It accepts input like "low light succulent" or "air-purifying pet safe" and dynamically returns matching plants. Each plant result is paired with a personalized seasonal care summary based on the current date.

### Key Features
- A highly curated CSV of 30+ plants
- Smart partial-matching search tool
- Terminal-friendly output styled with emojis
- Seasonal breakdown based on current date
- Fully dynamic, randomized test suite for quality assurance

---

## 💡 Why This Project?
This tool was designed to fulfill the Week 07 Prove Assignment's goal of showcasing modular design, data structure handling, and realistic conditional logic. Rather than simulating a product, the intent was to demonstrate deep understanding of course material with a focus on function reuse, input validation, and real-world data handling.

Robust search logic, careful plant data curation, and fully automated testing reinforce the overall quality. The core of the project is the dynamic fuzzy search system, capable of interpreting imperfect user input and surfacing relevant results.

---

## 📁 Included Project Files
- **"main.py"** — Core application logic with interactive prompts, dynamic search, and seasonal formatting.
- **"plants.csv"** — Curated plant database containing:
  - Name, category, water and light needs
  - Traits, seasonal care tips, and detailed plant advice
- **"test_plant_care.py"** — Advanced test file that:
  - Pulls random plants
  - Matches on name, traits, and partial fragments
  - Confirms failure on invalid/nonsense queries
- **"Flowchart.jpeg"** — Visual map of the program’s logic flow and functional transitions.
- **"project-report.txt"** — Time log documenting over 14 hours of work, categorized by planning, coding, curation, and testing.
- **"proposal.txt"** — Original idea submission.
- **"pyproject.toml"** — Pytest configuration file.

---

## 🧭 Flowchart Insight
To see how the logic comes together, open **"Flowchart.jpeg"**. It diagrams:
- Function calls
- User choices
- Search loops and exits
- Seasonal logic trees

It was used to help guide the structure before coding, ensuring modularity and clarity.

---

## ✅ Testing Overview
The test suite was built not just to pass checks—but to demonstrate real behavioral understanding. It dynamically selects random plants and traits, then verifies behavior through a series of checks.

### How to Run the Tests
```bash
python -m pytest -s test_plant_care.py
```

### What the Test Covers:
- 🔍 Matching plant names (e.g., "Pothos")
- 🌿 Matching full and partial traits (e.g., "low light" or "trailing")
- ❌ Ensuring invalid input returns no results

### Sample Output
```plaintext
🌿 Target Plant: ZZ Plant
🔎 Trait used for search: 'hardy'

📘 Name Search:
🔢 Results found: 3
✅ Name match test passed

🌿 Trait Fragment Search:
🔢 Results found: 2
✅ Trait fragment match test passed

🧪 Nonsense Search:
🔢 Results found: 0
✅ Nonsense test passed 🎉
```

Every test run is unique—allowing for wide coverage and confidence in stability.

---

## 🧪 How to Run the Program
Make sure you're in the correct directory, then run:
```bash
python main.py
```

### Example Flow
1. Type something like:
   ```plaintext
   low light pet safe
   ```
2. Choose a plant from the results by number
3. View a seasonal summary based on today's date
4. Return to main menu or exit

---

## 🔄 Example Use Cases
- `low light trailing` → Finds Pothos; shows spring watering tips.
- `fuzzy kid-friendly` → Returns Panda Plant; includes warning for overwatering.
- `sun drought-resistant` → Returns Yucca or Echeveria with heat-tolerant care.

---

## 📌 Final Summary
This tool was built from the ground up to meet the expectations of the CSE 111 Week 07 Final Project. Every function is modular. Every plant entry is individually reviewed. Every test is dynamic, randomized, and self-reporting.

The search algorithm supports partial and trait-based input. The care guide changes by season. The entire user experience is intuitive and emoji-enhanced for readability.

It’s not just code that runs—it’s logic that proves mastery.

---
