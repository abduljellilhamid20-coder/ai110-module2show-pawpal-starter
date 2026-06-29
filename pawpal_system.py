from dataclasses import dataclass, field
from typing import List
from datetime import date, timedelta


@dataclass
class Task:
    """Represents a single pet care activity."""
    description: str
    time: str          # format "HH:MM"
    duration: int      # in minutes
    priority: str      # "high", "medium", "low"
    frequency: str     # "once", "daily", "weekly"
    completed: bool = False
    due_date: date = field(default_factory=date.today)

    def mark_complete(self):
        """Mark this task as complete and reschedule if recurring."""
        self.completed = True
        return self.reschedule()

    def reschedule(self):
        """Create next occurrence for recurring tasks."""
        if self.frequency == "daily":
            return Task(
                description=self.description,
                time=self.time,
                duration=self.duration,
                priority=self.priority,
                frequency=self.frequency,
                due_date=self.due_date + timedelta(days=1)
            )
        if self.frequency == "weekly":
            return Task(
                description=self.description,
                time=self.time,
                duration=self.duration,
                priority=self.priority,
                frequency=self.frequency,
                due_date=self.due_date + timedelta(weeks=1)
            )
        return None


@dataclass
class Pet:
    """Represents a pet owned by an Owner."""
    name: str
    breed: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        """Add a task to this pet's list."""
        self.tasks.append(task)

    def get_tasks(self):
        """Return all tasks for this pet."""
        return self.tasks


class Owner:
    """Represents a pet owner who manages multiple pets."""

    def __init__(self, name: str):
        """Initialize owner with a name and empty pet list."""
        self.name = name
        self.pets: List[Pet] = []  # list of Pet objects

    def add_pet(self, pet: Pet):
        """Add a pet to this owner's list."""
        self.pets.append(pet)

    def get_all_tasks(self):
        """Return all tasks across all pets."""
        all_tasks = []
        for pet in self.pets:
            for task in pet.get_tasks():
                all_tasks.append((pet.name, task))
        return all_tasks


class Scheduler:
    """The brain that organizes and manages tasks."""

    def __init__(self, owner: Owner):
        """Initialize scheduler with an owner."""
        self.owner = owner

    def sort_by_time(self):
        """Return all tasks sorted by time."""
        all_tasks = self.owner.get_all_tasks()
        return sorted(all_tasks, key=lambda x: x[1].time)

    def filter_tasks(self, pet_name=None, completed=None):
        """Filter tasks by pet name or completion status."""
        tasks = self.owner.get_all_tasks()
        if pet_name:
            tasks = [(p, t) for p, t in tasks if p == pet_name]
        if completed is not None:
            tasks = [(p, t) for p, t in tasks if t.completed == completed]
        return tasks

    def detect_conflicts(self):
        """Find tasks scheduled at the same time."""
        all_tasks = self.owner.get_all_tasks()
        seen_times = {}
        conflicts = []
        for pet_name, task in all_tasks:
            if task.time in seen_times:
                conflicts.append(
                    f"⚠️ Conflict at {task.time}: '{task.description}' ({pet_name}) "
                    f"conflicts with '{seen_times[task.time][1].description}' "
                    f"({seen_times[task.time][0]})"
                )
            else:
                seen_times[task.time] = (pet_name, task)
        return conflicts

    def get_todays_schedule(self):
        """Return sorted tasks for today."""
        return self.sort_by_time()