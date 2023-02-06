from abc import ABCMeta, abstractclassmethod

from jinja2 import Environment, FileSystemLoader

class EmailModelBase(metaclass=ABCMeta):
    def __init__(self, config: dict[str, str]) -> None:
        self.send_email = config["send_email"]
        self.get_email = config["get_email"]
        self.author_code = config["author_code"]
        self.send_name = config["send_name"]
        self.template_path = config["template_path"]
        
    @abstractclassmethod
    def render_template(self, contents: dict[str, str]) -> str:
        pass

class EmailModel(EmailModelBase):
        
    def render_template(self, contents: dict[str, str]) -> str:
        env = Environment(loader=FileSystemLoader("./"))
        template = env.get_template(self.template_path)
        return template.render(contents)
        