# Create a venv
python -m venv venv_name

# Load these modules to the freshly created virtual env
pip install jupyter ipykernel

# Create another kernel for this venv
python -m ipykernel install --user --name=my_new_env --display-name "Python (my_new_env)"
