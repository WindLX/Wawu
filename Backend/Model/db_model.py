from __future__ import annotations
from dataclasses import dataclass
from abc import abstractclassmethod, ABCMeta

@dataclass
class DBModel(metaclass=ABCMeta):
    timeID: str
    
    @abstractclassmethod
    def serialize(self) -> tuple:
        pass

@dataclass
class TodoModel(DBModel):
    done: bool
    message: str
    endTime: str
    
    def serialize(self) -> tuple:
        return (self.timeID, self.done, self.message, self.endTime)
    
    @staticmethod
    def build(todo_tuple: tuple) -> TodoModel:
        return TodoModel(
            timeID=todo_tuple[0],
            done=todo_tuple[1],
            message=todo_tuple[2],
            endTime=todo_tuple[3]
        )