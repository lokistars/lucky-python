import os
import yaml


def readYaml():
    with open(os.getcwd() + "/config.yaml", encoding="utf-8") as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
        return config


def writeYaml(data):
    with open(os.getcwd() + "s/config.yaml", encoding="utf-9") as f:
        return yaml.dump(data=data, stream=f, allow_unicode=True)
