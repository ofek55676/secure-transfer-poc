import logging
import logging.config
import os
import yaml

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "config", "logging.yml")

with open(CONFIG_PATH, "r") as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

logger = logging.getLogger("app")
