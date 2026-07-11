# PART 2 — .gitignore
- Purpose: Batata hai Git ko kaunsi files/folders track NAHI karni. Ye tab banaya jata hai jab project setup karte ho — pehle hi commit se pehle.

> Kaise banate ho:
touch .gitignore

> Typical content (Python project ke liye):
__pycache__/
*.pyc
.env
venv/
.vscode/

> Kyun:
__pycache__/, *.pyc → Python auto-generated compiled files, repo mein junk hoti hain
.env → secrets/passwords — agar ye commit ho gaya toh security leak ho sakta hai (interview mein bohot pucha jata hai!)
venv/ → virtual environment folder, bohot bada hota hai, har developer apna khud banata hai

> Agar na banao: 
Tumhara repo garbage files se bhar jayega, aur agar .env accidentally push ho gaya toh production credentials leak ho sakte hain — real security incident.
Interview Q: ".env file accidentally commit ho gayi, kaise remove karoge history se?" → Answer: git rm --cached .env + BFG Repo-Cleaner/git filter-branch for full history cleanup.


# PART 3 — requirements.txt

> Purpose: 
Python project ki saari dependencies (external libraries) ek jagah list karta hai, taaki koi bhi developer/CI system ek command se same environment setup kar sake.

> Kab banate ho: 
Jab project mein external packages use karte ho (jaise flask, pytest, requests).
> Kaise banate ho:
pip freeze > requirements.txt

> Ya manually likho:
flask==2.3.2
pytest==7.4.0
requests==2.31.0

> Line-by-line meaning:

package==version → exact version pin karna (reproducibility ke liye)
== fixed version, >= minimum version — dono ka use case alag hai

Why exact version pin karte hain: Agar version pin nahi kiya toh "works on my machine" problem aati hai — kisi aur system pe naya version aake breaking changes la sakta hai.
Effect of missing: CI pipeline mein pip install -r requirements.txt fail ho jayega, ya galat versions install hoke bugs aayenge.
Interview Q: requirements.txt vs Pipfile vs poetry.lock mein kya difference hai?


# PART 4 — main.py
> Purpose: 
Application ka entry point — jaha se program execution start hoti hai.
Typical structure:
pythondef add(a, b):
    return a + b

if __name__ == "__main__":
    print(add(2, 3))

- Meaning of if __name__ == "__main__": — ye check karta hai ki file directly run ho rahi hai ya kisi aur file se import ho rahi hai. Isse test files mein function import karna safe rehta hai (bina extra code run kiye).

- Effect of removing this check: Jab test_main.py isko import karega, print(add(2,3)) bhi automatically run ho jayega — unwanted side effect.


# PART 5 — test_main.py
- Purpose: main.py ke functions ko automated testing ke through verify karna — CI pipeline isी file ko run karti hai.

from main import add

def test_add():
    assert add(2, 3) == 5

> Meaning:

- from main import add → main.py se function import
- def test_add(): → pytest convention hai test_ prefix se function naam start karna (pytest auto-discover karta hai)
- assert → condition check, false hone pe test fail

Why important in CI: Ye woh file hai jo .yml file ke pytest test_main.py step mein actually run hoti hai — agar koi bug aaya toh yeh pipeline ko red kar dega, merge block hoga.
Interview Q: Unit test vs Integration test mein kya farak hai? pytest kaise auto-discover karta hai test files ko?

Full Execution Flow (Sab Combine)
Developer code likhta hai (main.py)
        │
        ▼
Tests likhta hai (test_main.py)
        │
        ▼
Dependencies note karta hai (requirements.txt)
        │
        ▼
Junk files ignore karta hai (.gitignore)
        │
        ▼
git add . → git commit → git push origin main
        │
        ▼
GitHub detects .github/workflows/ci.yml
        │
        ▼
CI pipeline run: install deps → run tests
        │
        ▼
✅ / ❌ result GitHub Actions tab pe dikhta hai

Memory Trick
"D.I.M.R.T" yaad rakho pura setup:

Dependencies (requirements.txt) → Ignore (.gitignore) → Main code (main.py) → Rules (workflow.yml) → Tests (test_main.py)