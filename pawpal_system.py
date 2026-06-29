from dataclasses import dataclass, field
from typing import List
from datetime import date, timedelta


@dataclass
class Task:
    """Represents a single pet care activity."""
    description: str
    time: str  # format "HH:MM"
    duration: int  # in minutes
    priority: str  # "high", "medium", "low"
    frequency: str  # "once", "daily", "weekly"
    completed: bool = False
    due_date: date = field(default_factory=date.today)

    def mark_complete(self):
        """Mark this task as complete."""
        pass

    def reschedule(self):
        """Create next occurrence for recurring tasks."""
        pass


@dataclass
class Pet:
    """Represents a pet owned by an Owner."""
    name: str
    breed: str
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        """Add a task to this pet's list."""
        pass

    def get_tasks(self):
        """Return all tasks for this pet."""
        pass


class Owner:
    """Represents a pet owner who manages multiple pets."""

    def __init__(self, name: str):
        self.name = name
        self.pets: List[Pet] = []

    def add_pet(self, pet: Pet):
        """Add a pet to this owner's list."""
        pass

    def get_all_tasks(self):
        """Return all tasks across all pets."""
        pass


class Scheduler:
    """The brain that organizes and manages tasks."""

    def __init__(self, owner: Owner):
        self.owner = owner

    def sort_by_time(self):
        """Return all tasks sorted by time."""
        pass

    def filter_tasks(self, pet_name=None, completed=None):
        """Filter tasks by pet name or completion status."""
        pass

    def detect_conflicts(self):
        """Find tasks scheduled at the same time."""
        pass

    def get_todays_schedule(self):
        """Return sorted tasks for today."""
        pass