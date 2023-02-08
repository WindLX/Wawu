# from datetime import date, datetime
# from time import time
# from Service import EmailService, TodoService
# from Model import TodoModel, TodoConditionModel
# from Utils.wawu_logger import logger_init

# logger_init()
# e = EmailService()
# contents = {
#     "content": "这是测试文本",
#     "time": date.today()
# }
# pictures = {
#     "pic0": "pic0",
#     "pic1": "pic1",
#     "pic2": "pic2",
#     "pic3": "pic3",
# }

# todoConditionModel = TodoConditionModel(
#     startTime=None, 
#     endTime=None, 
#     done=True
# )

# new_todo = TodoModel(time(), False, "睡觉", datetime.now().strftime("%Y-%m-%d"))
# new_todo2 = TodoModel(time(), False, "吃饭", "2020-10-14")
# new_todo3 = TodoModel(time(), True, "玩游戏", "2002-01-01")
# # new_todo = TodoModel(time(), "你好", False, "2023-2-7 00:00:00")
# with TodoService() as d:
#     # d.add(new_todo3)
#     # d.delete("1675825586.29105")
#     # d.update("1675786590.803551", new_todo)
#     print(d.query(todoConditionModel))

from Core import app

if __name__ == "__main__":
    app.run()
    