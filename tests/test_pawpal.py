import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pawpal_system import Task, Pet, Owner, Scheduler
from datetime import date


def test_task_completion():
    """Test that marking a task complete changes its status."""
    task = Task(
        description="Morning walk",
        time="08:00",
        duration=30,
        priority="high",
        frequency="once"
    )
    assert task.completed == False
    task.mark_complete()
    assert task.completed == True


def test_add_task_increases_count():
    """Test that adding a task increases the pet's task count."""
    pet = Pet(name="Biscuit", breed="Golden Retriever")
    assert len(pet.get_tasks()) == 0
    pet.add_task(Task(
        description="Feeding",
        time="09:00",
        duration=10,
        priority="high",
        frequency="daily"
    ))
    assert len(pet.get_tasks()) == 1


def test_sort_by_time():
    """Test that tasks are returned in chronological order."""
    owner = Owner(name="Abduljellil")
    pet = Pet(name="Biscuit", breed="Golden Retriever")
    pet.add_task(Task("Evening walk", "18:00", 30, "medium", "daily"))
    pet.add_task(Task("Morning walk", "08:00", 30, "high", "daily"))
    pet.add_task(Task("Medication", "12:00", 5, "high", "daily"))
    owner.add_pet(pet)
    scheduler = Scheduler(owner)
    sorted_tasks = scheduler.sort_by_time()
    times = [t.time for _, t in sorted_tasks]
    assert times == ["08:00", "12:00", "18:00"]


def test_conflict_detection():
    """Test that scheduler detects tasks at the same time."""
    owner = Owner(name="Abduljellil")
    pet = Pet(name="Biscuit", breed="Golden Retriever")
    pet.add_task(Task("Morning walk", "08:00", 30, "high", "daily"))
    pet.add_task(Task("Feeding", "08:00", 10, "high", "daily"))
    owner.add_pet(pet)
    scheduler = Scheduler(owner)
    conflicts = scheduler.detect_conflicts()
    assert len(conflicts) > 0


def test_recurring_task():
    """Test that a daily task reschedules to the next day."""
    task = Task(
        description="Feeding",
        time="09:00",
        duration=10,
        priority="high",
        frequency="daily",
        due_date=date(2026, 6, 29)
    )
    next_task = task.mark_complete()
    assert next_task is not None
    assert next_task.due_date == date(2026, 6, 30)