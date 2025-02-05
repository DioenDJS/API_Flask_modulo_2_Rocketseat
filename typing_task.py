from dataclasses import dataclass

@dataclass
class TaskTyping:
    id: str
    title: str
    description: str
    completed: bool