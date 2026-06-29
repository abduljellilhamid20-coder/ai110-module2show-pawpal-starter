# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output

```
📅 Today's Schedule for Abduljellil:
=============================================
⬜ 08:00 — Morning walk (Biscuit) [high] 30min
⬜ 08:00 — Feeding (Whiskers) [high] 10min
⬜ 09:00 — Feeding (Biscuit) [high] 10min
⬜ 12:00 — Medication (Whiskers) [high] 5min
⬜ 18:00 — Evening walk (Biscuit) [medium] 30min

⚠️  Conflict Check:
=============================================
⚠️ Conflict at 08:00: 'Feeding' (Whiskers) conflicts with 'Morning walk' (Biscuit)

🐕 Biscuit's Tasks Only:
=============================================
  08:00 — Morning walk
  09:00 — Feeding
  18:00 — Evening walk
```

## 🧪 Testing PawPal+

```bash
# Run the full test suite:
pytest

# Run with coverage:
pytest --cov
```

Sample test output:

```
platform darwin -- Python 3.9.12, pytest-8.4.2
collected 5 items

tests/test_pawpal.py::test_task_completion PASSED        [ 20%]
tests/test_pawpal.py::test_add_task_increases_count PASSED [ 40%]
tests/test_pawpal.py::test_sort_by_time PASSED           [ 60%]
tests/test_pawpal.py::test_conflict_detection PASSED     [ 80%]
tests/test_pawpal.py::test_recurring_task PASSED         [100%]

5 passed in 0.02s
```

## 📐 Smarter Scheduling

> Fill in once you've implemented scheduling logic.

| Feature | Method(s) | Notes |
|---------|-----------|-------|
| Task sorting |       Scheduler.sort_by_time() |     puts tasks in order from earliest to latest |
| Filtering |      Scheduler.filter_tasks() | lets you see tasks for one pet or only unfinished ones |
| Conflict handling | Scheduler.detect_conflicts() |      gives a warning if two tasks are at the same time |
| Recurring tasks | Task.reschedule() |      automatically creates the next task when a daily one is done |

## 📸 Demo Walkthrough

Describe your app in numbered steps so a reader can follow along without watching a video:

1. User enters their name and adds a pet with a name and breed
2. User adds tasks to their pet like a morning walk at 08:00 or feeding at 09:00
3. The scheduler sorts all tasks by time and shows today's full schedule
4. If two tasks are at the same time, the app shows a conflict warning
5. When a daily task is marked complete, a new one is automatically created for the next day

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or link to a demo video here -->
