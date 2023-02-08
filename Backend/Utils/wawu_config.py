import json

from Utils import ConfigType

import yaml


class WawuConfig:
    def __init__(self, config_path: str, config_type: ConfigType) -> None:
        self.config_path = config_path
        self.config_type = config_type
        
    def get_config(self) -> dict[str, str]:
        with open(self.config_path, encoding="utf-8") as f:
            if self.config_type == ConfigType.yaml:
                return yaml.load(f, Loader=yaml.FullLoader)
            elif self.config_type == ConfigType.json:
                return json.load(f)
            else:
                raise TypeError("Unvalid ConfigType, either yaml nor json")
