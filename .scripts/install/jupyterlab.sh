#!/bin/sh
uv tool install jupyterlab \
  --with jupyter-bokeh \
  --with jupyterlab-code-formatter \
  --with jupyterlab-git \
  --with jupyterlab-hdf \
  --with jupyterlab-lsp \
  --with jupyterlab-myst \
  --with jupyterlab-myst \
  --with pyright \
  --with jupyterlab-vim \
  --with myst-nb \
  --with nbstripout \
  --with ipympl \
  --force

ln -sf ~/Library/Jupyter/kernels ~/.local/share/uv/tools/jupyterlab/share/jupyter/kernels
