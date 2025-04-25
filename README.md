# python-playground

An example dev project for Python 3 with Poetry

## Getting Started

```bash
# Run the script.
poetry run python src/main.py
```

## Project Description

* Python version can be specified using the image tag of the dev container.
  * Tags which specify Python minor versions like below are recommended if there are no specific requirements.
  `mcr.microsoft.com/devcontainers/python:3.12`
  * Refer to the [naming convention](https://github.com/devcontainers/images/tree/main/src/python#configuration) of the tags and [the list of available tags](https://mcr.microsoft.com/v2/devcontainers/python/tags/list).
* Additional VS Code extensions are listed in `devcontainer.json`
  ```json
  {
    "customizations": {
      "vscode": {
        "extensions": [
          "ms-python.black-formatter",
          "njpwerner.autodocstring"
        ]
      }
	}
  ```
* Poetry is installed in `postCreateCommand`.
* Poetry configuration resides in `poetry.toml`.
  * Currently, there is only one configuration [`virtualenvs.prompt`](https://python-poetry.org/docs/configuration/#virtualenvsprompt) to shorten the shell prompt.

## How to use with Docker on WSL2

1. Open the project in WSL2 mode. This can be done either of the following steps;
   * Open the WSL2 terminal and execute `code /path/to/project`.
   * Open the project folder in WSL2 directory under `\\wsl.localhost` with VS Code, and open the command palette (`Ctrl + Shift + P`) to select `Dev Containers: Reopen in WSL2`.
2. Open the command palette (`Ctrl + Shift + P`) and select `Dev Containers: Reopen in Container`. 
