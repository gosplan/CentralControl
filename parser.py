import os

import yaml


GOSPLAN_DIR = os.path.join(os.getcwd(), 'gosplans')


def parse_gosplans():
    gosplan_names = set()
    gosplan_configs = {}

    for filename in os.listdir(GOSPLAN_DIR):
        with open(os.path.join(GOSPLAN_DIR, filename), 'r') as f:
            config = yaml.safe_load(f.read())

            if 'name' in config:
                gosplan_names.add(config['name'])
                gosplan_configs[config['name']] = config

    return gosplan_names, gosplan_configs
