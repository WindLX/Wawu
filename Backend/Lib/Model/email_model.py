from jinja2 import Environment, FileSystemLoader


class EmailModel:
    def __init__(self, config: dict[str, str]) -> None:
        self.send_email = config["send_email"]
        self.get_email = config["get_email"]
        self.author_code = config["author_code"]
        self.send_name = config["send_name"]
        self.template_path = config["template_path"]
        
    def render_template(self, contents: dict[str, str]) -> str:
        env = Environment(loader=FileSystemLoader("./"))
        template = env.get_template(self.template_path)
        return template.render(contents)
    
    def dict(self) -> dict:
        return dict(
            send_email=self.send_email,
            get_email=self.get_email,
            author_code=self.author_code,
            send_name=self.send_name,
            template_path=self.template_path
        )
        