from pawpal_system import Task, Pet, Owner, Scheduler
from datetime import date

# Create an owner
owner = Owner(name="Abduljellil")

# Create two pets
dog = Pet(name="Biscuit", breed="Golden Retriever")
cat = Pet(name="Whiskers", breed="Tabby Cat")

# Add tasks to Biscuit
dog.add_task(Task(
    description="Morning walk",
    time="08:00",
    duration=30,
    priority="high",
    frequency="daily"
))
dog.add_task(Task(
    description="Feeding",
    time="09:00",
    duration=10,
    priority="high",
    frequency="daily"
))
dog.add_task(Task(
    description="Evening walk",
    time="18:00",
    duration=30,
    priority="medium",
    frequency="daily"
))

# Add tasks to Whiskers
cat.add_task(Task(
    description="Feeding",
    time="08:00",  # same time as Biscuit's walk - conflict!
    duration=10,
    priority="high",
    frequency="daily"
))
cat.add_task(Task(
    description="Medication",
    time="12:00",
    duration=5,
    priority="high",
    frequency="daily"
))

# Add pets to owner
owner.add_pet(dog)
owner.add_pet(cat)

# Create scheduler
scheduler = Scheduler(owner)

# Print today's schedule
print(f"\n📅 Today's Schedule for {owner.name}:")
print("=" * 45)
for pet_name, task in scheduler.get_todays_schedule():
    status = "✅" if task.completed else "⬜"
    print(f"{status} {task.time} — {task.description} ({pet_name}) "
          f"[{task.priority}] {task.duration}min")

# Print conflicts
print("\n⚠️  Conflict Check:")
print("=" * 45)
conflicts = scheduler.detect_conflicts()
if conflicts:
    for c in conflicts:
        print(c)
else:
    print("No conflicts found!")

# Test filtering
print("\n🐕 Biscuit's Tasks Only:")
print("=" * 45)
for pet_name, task in scheduler.filter_tasks(pet_name="Biscuit"):
    print(f"  {task.time} — {task.description}")