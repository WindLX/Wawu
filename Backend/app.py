from datetime import date
from Server import EmailServer
from Utils.wawu_logger import logger_init

logger_init()
e = EmailServer()
contents = {
    "content": "这是测试文本",
    "time": date.today()
}
pictures = {
    "pic0": "pic0",
    "pic1": "pic1",
    "pic2": "pic2",
    "pic3": "pic3",
}
e.send("测试", contents, pictures)