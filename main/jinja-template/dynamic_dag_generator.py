from jinja2 import Environment, FileSystemLoader
import os
import yaml 

# Get name of the directory, __file__ will pass the python file name
file_dir = os.path.dirname(os.path.abspath(__file__)) 
# print(filr_dir)

# Create Jinja2 environment
env = Environment(loader=FileSystemLoader(file_dir))

# Pass template name to the Jinja2 environment
template=env.get_template('template_dag.jinja2')

for file_name in os.listdir(file_dir):
    if file_name.endswith(".yml"):
        # read config file
        with open(f"{file_dir}/{file_name}","r") as configfile:

            # get config yaml file data
            config = yaml.safe_load(configfile)
            # print(type(config)) # config type should be dict
            # print(config) # check config values

            # create a dag file using the jinja2 template
            with open(f"{file_dir}/generated-dags/{config["dag_id"]}.py","w") as dagfile:
                dagfile.write(template.render(config))


