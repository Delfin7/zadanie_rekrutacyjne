from dataclasses import dataclass


@dataclass
class Task:
    title: str
    description: str
    environment: str
    version: str
    deadline: str