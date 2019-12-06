import os

import yaml


GOSPLAN_DIR = os.path.join(os.getcwd(), 'gosplans')


def parse_gosplans():
    for filename in os.listdir(GOSPLAN_DIR):
        with open(os.path.join(GOSPLAN_DIR, filename), 'r') as f:
            config = yaml.safe_load(f.read())

            #TODO call Finlay's thing with the config??
