import logging
from time import time

from Service import TodoService
from Model import TodoModel, TodoConditionModel

from flask import request, Blueprint


todo = Blueprint("todo", __name__)

@todo.route("/api/todo/query", methods=['GET'])
def query_todo():
    try:
        condition = None
        if request.json is not None:
            condition = TodoConditionModel.build(request.json)
    except Exception as e:
        logging.getLogger("server").warning(f"错误的查询格式({e})")
    with TodoService() as todo_service:
        query_result = todo_service.query(condition)
    return query_result

@todo.route("/api/todo/add", methods=['POST'])
def add_todo():
    new_todo = TodoModel(timeID=time(), done=False, message=request.json["message"], endTime=request.json["endTime"])
    with TodoService() as todo_service:
        res = todo_service.add(new_todo)
    return "Add Successfully" if res else "Add in Failure"

@todo.route("/api/todo/delete", methods=["DELETE"])
def delete_todo():
    target_todo_timeID = request.json["timeID"]
    with TodoService() as todo_service:
        res = todo_service.delete(target_todo_timeID)
    return "Delete Successfully" if res else "Delete in Failure"

@todo.route("/api/todo/update", methods=["PATCH"])
def update_todo():
    target_todo_timeID = request.json["timeID"]
    new_todo = TodoModel(timeID=time(), done=False, message=request.json["message"], endTime=request.json["endTime"])
    with TodoService() as todo_service:
        res = todo_service.update(target_todo_timeID, new_todo)
    return "Update Successfully" if res else "Update in Failure"
