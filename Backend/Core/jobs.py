import datetime

from Service import EmailService, TodoService
from Model import TodoConditionModel
from Utils import WawuConfig, ConfigType


def auto_send_email():
    with TodoService() as todo_service:
        target_time = (datetime.datetime.now() + datetime.timedelta(days=3)).strftime("%Y-%m-%d")
        res = todo_service.query(TodoConditionModel(done=False, startTime=datetime.datetime.now().strftime("%Y-%m-%d"), endTime=target_time))
        if any(res):
            content = ""
            time = ""
            for todo in res:
                content += f"{todo.message} "
                time += f"{todo.endTime} "
            subject = "待办事项提醒"
            contents = {
                "content": content,
                "time": time
            }
            pictures = WawuConfig(config_type=ConfigType.json, config_path="./Resources/Images/pictures.json").get_config()
            
            email_service = EmailService()
            email_service.send(subject, contents, pictures)
