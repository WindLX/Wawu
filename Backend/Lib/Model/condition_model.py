from __future__ import annotations
from dataclasses import dataclass
from abc import abstractclassmethod, ABCMeta
from typing import Optional


@dataclass
class ConditionModelBase(metaclass=ABCMeta):
    
    @abstractclassmethod
    def tuple(self) -> tuple:
        pass
    
    @abstractclassmethod
    def dict(self) -> dict:
        pass
    
    
@dataclass
class TodoConditionModel(ConditionModelBase):
    done: Optional[bool]
    startTime: Optional[str]
    endTime: Optional[str]

    def tuple(self) -> tuple:
        return (self.done, self.startTime, self.endTime)
    
    def dict(self) -> dict:
        return dict(done=self.done, startTime=self.startTime, endTime=self.endTime)
    
    @staticmethod
    def build(todo_condition: dict) -> TodoConditionModel:
        return TodoConditionModel(todo_condition["done"], todo_condition["startTime"], todo_condition["endTime"])
    