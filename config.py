import yaml
import os

def load_config(path):
    if os.path.exists(path) == False:
	raise ValueError('config file not found')

    if os.access(path, os.R_OK)==False:
	raise ValueError('no access to the config file')

    try:
        config = yaml.load(open(path))
    except yaml.YAMLError as exc:
	print(exc)
	exit(0)

    return config

