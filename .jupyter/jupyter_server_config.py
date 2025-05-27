c = get_config()  # noqa

c.ServerApp.open_browser = False
c.LanguageServerManager.autodetect = False
c.LanguageServerManager.language_servers = {
    "ruff": {
        "version": 2,
        "argv": ["ruff", "server"],
        "languages": ["python"],
        "mime_types": ["text/python", "text/ipython"],
        "display_name": "ruff",
    },
    "pyright": {
        "version": 2,
        "argv": ["pyright-langserver", "--stdio"],
        "languages": ["python"],
        "mime_types": ["text/python", "text/ipython"],
        "display_name": "pyright",
    },
}
