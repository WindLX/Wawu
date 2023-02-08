from dataclasses import dataclass
from abc import abstractclassmethod, ABCMeta
from typing import Optional

@dataclass
class ConditionModelBase(metaclass=ABCMeta):
    
    @abstractclassmethod
    def serialize(self) -> dict:
        pass
    
@dataclass
class TodoConditionModel(ConditionModelBase):
    done: Optional[bool]
    startTime: Optional[str]
    endTime: Optional[str]

    def serialize(self) -> dict:
        return (self.done, self.startTime, self.endTime)
    
    def dict(self) -> dict:
        return dict(done=self.done, startTime=self.startTime, endTime=self.endTime)