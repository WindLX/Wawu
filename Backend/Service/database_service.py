import sqlite3, logging
from abc import ABCMeta, abstractclassmethod

from Model import DBModel, TodoModel, ConditionModelBase, TodoConditionModel

class DataBaseService(metaclass=ABCMeta):
    def __init__(self) -> None:
        self.database: str = "./Data/wawu.db"
    
    def __enter__(self):
        self.database_conn = sqlite3.connect(self.database)
        self.cursor = self.database_conn.cursor()
        return self
        
    def __exit__(self, exec_type, exec_value, exec_tb):
        self.database_conn.commit()
        self.database_conn.close()
        if exec_tb:
            logging.error(f"数据库关闭异常(Type: {exec_type}, Value: {exec_value}, Traceback: {exec_tb})")
            logging.getLogger("server").error(f"数据库关闭异常(Type: {exec_type}, Value: {exec_value}, Traceback: {exec_tb})")
    
    @abstractclassmethod
    def add(self, new_data: DBModel) -> bool:
        pass

    @abstractclassmethod
    def delete(self, target_data_timeID: str) -> bool:
        pass

    @abstractclassmethod
    def update(self, target_data_timeID: str, new_data: DBModel) -> bool:
        pass

    @abstractclassmethod
    def query(self, condition: ConditionModelBase=None) -> list[DBModel]:
        pass
    
class TodoService(DataBaseService):
    
    def add(self, new_data: TodoModel) -> bool:
        sql = f"INSERT INTO [TodoList] VALUES(?, ?, ?, ?)"
        try:
            self.cursor.execute(sql, new_data.serialize())
            logging.info(f"添加新 Todo 成功({new_data.message})")
            logging.getLogger("server").info(f"添加新 Todo 成功({new_data.message})")
            return True
        except Exception as e:
            logging.error(f"添加新 Todo 异常 ({e})")
            logging.getLogger("server").error(f"添加新 Todo 异常({e})")
            return False
            
    def delete(self, target_data_timeID: str) -> bool:
        sql = f"DELETE FROM [TodoList] WHERE [TimeID] = ?"
        try:
            self.cursor.execute(sql, (target_data_timeID, ))
            logging.info(f"删除 Todo 成功({target_data_timeID})")
            logging.getLogger("server").info(f"删除 Todo 成功({target_data_timeID})")
            return True
        except Exception as e:
            logging.error(f"删除 Todo 异常 ({e})")
            logging.getLogger("server").error(f"删除 Todo 异常({e})")
            return False

    def update(self, target_data_timeID: str, new_data: TodoModel) -> bool:
        sql = f"UPDATE [TodoList] SET [Done] = ?, [Message] = ?, [EndTime] = ? WHERE [TimeID] = ?"
        try:
            self.cursor.execute(sql, new_data.serialize()[1:] + (target_data_timeID, ))
            logging.info(f"更改 Todo 成功({target_data_timeID}, {new_data.message})")
            logging.getLogger("server").info(f"更改 Todo 成功({target_data_timeID}, {new_data.message})")
            return True
        except Exception as e:
            logging.error(f"更改 Todo 异常 ({e})")
            logging.getLogger("server").error(f"更改 Todo 异常({e})")
            return False

    def query(self, condition: TodoConditionModel=None) -> list[TodoModel]:
        sql = f"SELECT * FROM [TodoList]"
        try:
            if condition is not None:
                if any(condition.serialize()):
                    sql = sql + " WHERE "
                    if condition.done is not None:
                        sql = sql + "[Done] = :done"
                        if all(condition.serialize()[1:]):
                            sql = sql + " AND [EndTime] >= :startTime AND [EndTime] <= :endTime"
                    elif all(condition.serialize()[1:]):
                        sql = sql + "[EndTime] >= :startTime AND [EndTime] <= :endTime"
                self.cursor.execute(sql, condition.dict())
            else:
                self.cursor.execute(sql)
            return [TodoModel.build(todo) for todo in self.cursor.fetchall()]
        except Exception as e:
            logging.error(f"查询 Todo 异常 ({e})")
            logging.getLogger("server").error(f"查询 Todo 异常({e})")
            return []
