#!/bin/sh
uv tool install jupyterhub \
  --with jupyter-bokeh \
  --with jupyterlab \
  --with jupyterlab-code-formatter \
  --with jupyterlab-git \
  --with jupyterlab-hdf \
  --with jupyterlab-lsp \
  --with jupyterlab-myst \
  --with jupyterlab-myst \
  --with jupyterlab-vim \
  --with myst-nb \
  --with nbstripout \
  --with ipympl

ln -sf ~/Library/Jupyter/kernels ~/.local/share/uv/tools/jupyterhub/share/jupyter/kernels
