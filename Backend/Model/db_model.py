from __future__ import annotations
from dataclasses import dataclass
from abc import abstractclassmethod, ABCMeta


@dataclass
class DBModel(metaclass=ABCMeta):
    timeID: str
    
    @abstractclassmethod
    def tuple(self) -> tuple:
        pass
    
    @abstractclassmethod
    def dict(self) -> dict:
        pass

@dataclass
class TodoModel(DBModel):
    done: bool
    message: str
    endTime: str
    
    def tuple(self) -> tuple:
        return (self.timeID, self.done, self.message, self.endTime)
    
    def dict(self) -> dict:
        return dict(
            tiemID=self.timeID,
            done=self.done,
            message=self.message,
            endTime=self.endTime
        )
    
    @staticmethod
    def build(todo_tuple: tuple) -> TodoModel:
        return TodoModel(
            timeID=todo_tuple[0],
            done=todo_tuple[1],
            message=todo_tuple[2],
            endTime=todo_tuple[3]
        )