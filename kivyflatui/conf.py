from get_dir import get_dir
import os
import yaml
DIR=get_dir()
conf_path = os.path.join(DIR,'conf.yaml')
conf = yaml.load(open(conf_path))
