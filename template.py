import os
from pathlib import Path

project_name = "src"

list_of_files = [
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/config/__init__.py",
    f"{project_name}/config/configuration.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/logger/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "experiments.ipynb",
    "templates/index.html"
]


for filepath in list_of_files:
    filepath = Path(filepath)
    # we are using / but windows uses \, above line converts path into windows path 

    filedir, filename = os.path.split(filepath)
    # splits the filepath into dir and file

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        # exists_ok, i.e if exists then will not create

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
    else:
        print(f"file is already present at: {filepath}")