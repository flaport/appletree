c = get_config()  # noqa

c.ServerApp.open_browser = False
c.LanguageServerManager.autodetect = False
c.LanguageServerManager.language_servers = {
    "pyright": {
        "argv": ["pyright-langserver", "--stdio"],
        "languages": ["python"],
        "version": 2,
        "mime_types": ["text/python", "text/ipython"],
        "display_name": "pyright",
    },
    "pylsp": {
        "plugins": {
            "ruff": {
                "enabled": True,
                "formatEnabled": True,
                "executable": "ruff",
                "format": ["I"],
                "severities": {"D212": "I"},
                "unsafeFixes": True,
                "lineLength": 88,
                "preview": True,
                "targetVersion": "py312",
            },
            "autopep8": {"enabled": False},
            "flake8": {"enabled": False},
            "jedi": {"enabled": False},
            "jedi_completion": {"enabled": False},
            "jedi_definition": {"enabled": False},
            "jedi_hover": {"enabled": False},
            "jedi_references": {"enabled": False},
            "jedi_signature_help": {"enabled": False},
            "jedi_symbols": {"enabled": False},
            "preload": {"enabled": False},
            "pycodestyle": {"enabled": False},
            "pydocstyle": {"enabled": False},
            "pyflakes": {"enabled": False},
            "pylint": {"enabled": False},
            "rope_autoimport": {"enabled": False},
            "rope_completion": {"enabled": False},
            "yapf": {"enabled": False},
        },
    },
}
