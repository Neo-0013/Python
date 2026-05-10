# 🐍 Python Basics — For Everyone

> **No programming experience needed.** If you've ever written a lab report, used Excel, or followed a recipe — you already think like a programmer. This guide proves it.

---

## 📖 What is Python, really?

Imagine you want to teach your younger sibling to make a sandwich. You'd give them **step-by-step instructions** in plain English:

1. Take two slices of bread
2. Spread butter on one side
3. Add filling
4. Put the slices together

**Python is exactly that** — a way to give step-by-step instructions to a computer, written in something very close to plain English. The computer follows your instructions perfectly, every single time, without getting tired or making mistakes.

---

## 📂 What's in this folder?

| File | What it teaches | Real-world analogy |
|------|-----------------|--------------------|
| `hello-world.py` | Your first output | Saying "Hello" on day one of class |
| `var.py` | Variables & data types | Labelling test tubes in a lab |
| `Control-flow.py` | If/else decisions | A doctor's diagnosis flowchart |
| `loops.py` | Repeating actions | Pipetting 96 wells in a plate |
| `functions.py` | Reusable instructions | A lab protocol you run many times |
| `string_methods.py` | Working with text | Editing a DNA sequence |
| `list_methods.py` | Working with collections | Managing a list of specimens |
| `dictionaries.py` | Key-value data | A biological taxonomy reference book |

---

## 🧪 `hello-world.py` — Saying Hello

The very first thing every programmer learns. You're simply telling the computer to display a message.

```python
print("Hello, World!")
```

**Biology analogy:** This is like writing your name on a lab report. It's your way of saying *"I exist, I'm here, and I'm ready to work."*

`print()` is an instruction that means **"show this on screen."** Whatever you put inside the brackets gets displayed. That's it.

```python
print("Hello, World!")         # shows: Hello, World!
print("My name is Neo")        # shows: My name is Neo
print("Python is awesome!")    # shows: Python is awesome!
```

---

## 🏷️ `var.py` — Variables & Data Types

**What is a variable?**

In a biology lab, you label your test tubes. Tube A has blood sample. Tube B has saline. The **label** is a variable — it's a name that points to something stored inside.

```python
# Just like labelling test tubes:
patient_name = "Sarah"      # 🧪 Tube labelled "patient_name" contains "Sarah"
patient_age  = 28           # 🧪 Tube labelled "patient_age" contains 28
temperature  = 37.5         # 🧪 Tube labelled "temperature" contains 37.5
is_infected  = True         # 🧪 Tube labelled "is_infected" contains True
```

**The 4 basic types of data:**

| Type | What it holds | Example | Biology equivalent |
|------|--------------|---------|-------------------|
| `str` | Text (string) | `"ATCG"` | A DNA sequence written out |
| `int` | Whole numbers | `46` | Chromosome count |
| `float` | Decimal numbers | `98.6` | Body temperature |
| `bool` | True or False only | `True` | Is the test positive? |

```python
dna_sequence    = "ATCGATCG"   # str  — text
chromosome_count = 46          # int  — whole number
body_temp        = 37.5        # float — decimal
is_positive      = False       # bool — yes/no
```

> 💡 **Key insight:** Python figures out the type automatically. You don't have to tell it. Just assign and it knows.

---

## 🔀 `Control-flow.py` — Making Decisions

**What is control flow?**

When a doctor examines a patient, they follow a decision tree:
- *Is the temperature above 38°C?* → Yes → Likely fever
- *Is the throat red?* → Yes → Could be infection → Run a test
- *Is the test positive?* → Yes → Prescribe antibiotics

This is **exactly** what `if / elif / else` does in Python — it makes decisions based on conditions.

```python
temperature = 38.9

if temperature > 38.0:
    print("Fever detected — run further tests")
elif temperature > 37.5:
    print("Slightly elevated — monitor the patient")
else:
    print("Temperature normal — no action needed")
```

**How to read it:**
- `if` = "First, check this condition"
- `elif` = "If that wasn't true, check THIS instead" (short for "else if")
- `else` = "If none of the above were true, do this"

```python
# Real biology scenario — classifying a cell count
white_blood_cells = 11500   # cells per microlitre

if white_blood_cells > 11000:
    print("Leukocytosis — possible infection or inflammation")
elif white_blood_cells < 4500:
    print("Leukopenia — immune system may be compromised")
else:
    print("WBC count normal (4,500–11,000)")
```

The computer reads from top to bottom, checks each condition, runs the matching block, and skips the rest.

---

## 🔁 `loops.py` — Repeating Actions

**What is a loop?**

Imagine you're pipetting samples into a 6-well plate. You do the **exact same action** for each well — pick up pipette, draw sample, dispense, move to next well. You repeat until all wells are filled.

That repetitive action is a **loop.**

### The `for` loop — repeat a known number of times

```python
# Pipetting 6 wells — same action, repeated
wells = ["Well 1", "Well 2", "Well 3", "Well 4", "Well 5", "Well 6"]

for well in wells:
    print(f"Pipetting sample into {well}")

# Output:
# Pipetting sample into Well 1
# Pipetting sample into Well 2
# ... and so on
```

```python
# Using range() — like saying "do this 10 times"
for i in range(1, 11):
    print(f"Counting cell colony {i}")
```

### The `while` loop — repeat UNTIL a condition is met

```python
# Keep incubating until temperature reaches 37°C
current_temp = 25

while current_temp < 37:
    print(f"Incubating... current temp: {current_temp}°C")
    current_temp += 1    # temperature rises by 1 each cycle

print("Target temperature reached! Begin experiment.")
```

> 💡 **Rule of thumb:** Use `for` when you know how many times. Use `while` when you don't know — just repeat until a condition is met.

---

## ⚙️ `functions.py` — Reusable Instructions

**What is a function?**

In biology, a **Standard Operating Procedure (SOP)** is a written protocol for a common lab task — like how to prepare an agar plate, or how to extract DNA. You write it once, then any lab member can follow it anytime without rewriting it.

A Python **function** is the same thing. Write the instructions once, use them as many times as you want.

```python
# Writing the SOP (defining the function)
def prepare_agar_plate(bacteria_type, temperature):
    print(f"Preparing plate for: {bacteria_type}")
    print(f"Incubation temperature: {temperature}°C")
    print("Pouring agar... sealing plate... labelling...")
    print("Plate ready! ✅")

# Using the SOP (calling the function)
prepare_agar_plate("E. coli", 37)
prepare_agar_plate("S. aureus", 35)
prepare_agar_plate("Salmonella", 37)
```

**Functions that give you back a result:**

```python
# A function that calculates BMI and RETURNS the result
def calculate_bmi(weight_kg, height_m):
    bmi = weight_kg / (height_m ** 2)
    return bmi    # "return" means "give this value back to whoever called me"

# Now you can use the result
patient_bmi = calculate_bmi(70, 1.75)
print(f"BMI: {patient_bmi:.1f}")    # BMI: 22.9

if patient_bmi > 30:
    print("Classified as obese")
elif patient_bmi > 25:
    print("Classified as overweight")
else:
    print("Healthy BMI range")
```

> 💡 **Golden rule:** If you're copy-pasting the same block of code more than twice — turn it into a function.

---

## 🔤 `string_methods.py` — Working with Text

**What is a string?**

A string is any text — a word, a sentence, a DNA sequence, a patient name. It's always written inside quotes.

Think of a DNA strand: `"ATCGATCGTAGC"` — it's a sequence of characters, and you often need to search it, slice it, or modify it. Python strings work the same way.

```python
dna = "atcgatcgtagc"

# Make it uppercase (like how DNA is written in papers)
print(dna.upper())              # ATCGATCGTAGC

# How long is the sequence?
print(len(dna))                 # 12

# Does it contain a specific codon?
print("atg" in dna)            # True (ATG = start codon!)

# Find where a pattern starts
print(dna.find("tag"))         # 8 (stop codon found at position 8!)

# Replace a mutation
mutated = dna.replace("atc", "aaa")
print(mutated)                  # aaagaaaatagc

# Slice — extract just part of the sequence
codon_1 = dna[0:3]             # "atc" (positions 0, 1, 2)
codon_2 = dna[3:6]             # "gat"
print(codon_1, codon_2)
```

**The slice syntax explained:**
```
dna = "A T C G A T"
       0 1 2 3 4 5   ← position numbers

dna[0:3]  →  "ATC"   (from 0, up to but NOT including 3)
dna[3:6]  →  "GAT"
```

> 💡 Python starts counting from **0**, not 1. First character is position 0. This trips everyone up at first — totally normal!

---

## 📋 `list_methods.py` — Collections of Things

**What is a list?**

Imagine a museum has a collection of biological specimens — arranged in order in a cabinet. You can add new specimens, remove old ones, find a specific one, or sort them. 

That's a Python **list** — an ordered, changeable collection.

```python
# A list of specimens in the cabinet
specimens = ["Frog", "Butterfly", "Snake", "Eagle", "Shark"]

# Access by position (remember — starts at 0!)
print(specimens[0])       # Frog (first)
print(specimens[-1])      # Shark (last — negative means count from end)

# Add a new specimen
specimens.append("Wolf")
print(specimens)          # [..., "Shark", "Wolf"]

# Remove one
specimens.remove("Snake")

# Sort alphabetically
specimens.sort()
print(specimens)          # ['Butterfly', 'Eagle', 'Frog', 'Shark', 'Wolf']

# How many specimens?
print(len(specimens))     # 5

# Loop through all of them
for animal in specimens:
    print(f"Cataloguing: {animal}")
```

**Real lab scenario — tracking cell counts:**
```python
cell_counts = [1200, 1350, 980, 1500, 1100, 1420]

print(f"Highest count: {max(cell_counts)}")    # 1500
print(f"Lowest count:  {min(cell_counts)}")    # 980
print(f"Total cells:   {sum(cell_counts)}")    # 7550
print(f"Average:       {sum(cell_counts)/len(cell_counts):.0f}")  # 1258
```

---

## 📚 `dictionaries.py` — Lookup Tables

**What is a dictionary?**

A biology textbook has an **index** at the back. You look up "mitochondria" and it tells you everything about it — page number, definition, classification.

A Python dictionary works identically. You look something up by its **key** and get back its **value**.

```python
# Like a patient medical record
patient = {
    "name":       "Sarah Ahmed",
    "age":        28,
    "blood_type": "O+",
    "conditions": ["Asthma", "Hypertension"],
    "is_admitted": True
}

# Look things up by key
print(patient["name"])        # Sarah Ahmed
print(patient["blood_type"])  # O+
print(patient["conditions"])  # ['Asthma', 'Hypertension']

# Update a value
patient["age"] = 29

# Add a new field
patient["ward"] = "General"

# Check if a key exists before looking it up
if "allergies" in patient:
    print(patient["allergies"])
else:
    print("No allergies on record")
```

**Real use case — a species classification system:**
```python
taxonomy = {
    "Lion":      {"kingdom": "Animalia", "class": "Mammalia", "endangered": False},
    "Snow Leopard": {"kingdom": "Animalia", "class": "Mammalia", "endangered": True},
    "Blue Whale": {"kingdom": "Animalia", "class": "Mammalia", "endangered": True},
}

for species, info in taxonomy.items():
    status = "⚠️ ENDANGERED" if info["endangered"] else "✅ Stable"
    print(f"{species}: {status}")
```

> 💡 **Lists vs Dictionaries:**
> - **List** = a numbered drawer system (access by position: `specimens[0]`)
> - **Dictionary** = a labelled filing cabinet (access by name: `patient["name"]`)

---

## 🧠 The Big Picture — How It All Connects

```
Variables    →  Store individual pieces of data (one test tube)
Lists        →  Store collections of data (a rack of test tubes)
Dictionaries →  Store labelled data (a filing cabinet)
Control Flow →  Make decisions based on data (doctor's diagnosis)
Loops        →  Repeat actions on data (processing all 96 wells)
Functions    →  Package reusable instructions (lab SOPs)
Strings      →  Work with text and sequences (DNA analysis)
```

Think of a complete Python program like a **full lab experiment:**
- Variables are your labelled samples
- Functions are your SOPs
- Loops are your repetitive pipetting steps
- Control flow is your decision-making based on results
- Dictionaries are your data recording sheets

---

## 🚀 How to Run These Files

You need Python installed — [download here](https://www.python.org/downloads/) (takes 2 minutes).

Then open your terminal and type:

```bash
# Run any file like this:
python hello-world.py
python var.py
python loops.py
```

You'll see the output printed right in your terminal.

---

## 💡 Tips for Complete Beginners

1. **Read the code out loud.** Python is close to English — reading it aloud helps it click.
2. **Change things and see what happens.** Break it deliberately. That's how you learn fastest.
3. **Errors are not failures.** Every error message is Python telling you exactly what went wrong and where.
4. **One concept per day is enough.** Don't rush. Even professional developers Googled the basics for years.

---

## 📬 Questions?

Open an [Issue](../../issues) on this repo — no question is too basic. If a biology student can't understand an explanation in here, that's a bug in the README, not a bug in the student.

---

*Made with 🐍 and ☕ by [Neo-0013](https://github.com/Neo-0013)*
