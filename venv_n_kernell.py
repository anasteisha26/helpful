# Create a venv
python -m venv venv_name

# Load these modules to the freshly created virtual env
pip install jupyter ipykernel

# Create another kernel for this venv
python -m ipykernel install --user --name=my_new_env --display-name "Python (my_new_env)"

# see all available kernels
jupyter kernelspec list

# remove unnecessary kernel
jupyter kernelspec remove myenv

# or if upper doesn't work:
jupyter-kernelspec uninstall myenv

# check if it was removed
jupyter kernelspec list

# remove outdated venv
rm -rf path/to/venv
