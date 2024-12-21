from yaml import load, CSafeLoader
from pydantic import BaseModel


def _parse_config_file() -> dict:
    with open("config.yml") as file:
        return load(file, CSafeLoader)


def get_config(model: type[BaseModel], root_key: str) -> BaseModel.model_validate:
    config_dict = _parse_config_file()
    if root_key not in config_dict:
        error = f"key {root_key} not found in bot config"
        raise ValueError(error)
    return model.model_validate(config_dict[root_key])
