# FlashV3 Model

## ENV SETUP

```
virtualenv .flashV3-model
source .flashV3-model/bin/activate
git init
pip install jupyterlab jupyterthemes jupyterlab_darkside_ui cadCAD cadCAD_diagram matplotlib pandas plotly ipywidgets numpy networkx scipy seaborn python-dotenv psycopg2 psycopg2-binary statsmodels
jupyter labextension install jupyterlab-plotly
python -m ipykernel install --user --name=.flashV3-model
```

```
mkdir model && cd model
touch __init__.py
touch  config.py
touch  partial_state_update_block.py
touch  run.py
touch  sim_params.py
touch  state_variables.py
touch  sys_params.py
mkdir parts && cd parts
touch __init__.py
```

## RUN

```
jupyter-lab
jupyter notebook [OLD]
```
