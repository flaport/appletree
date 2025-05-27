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
    "ruff": {
        "argv": ["ruff", "server"],
        "languages": ["python"],
        "version": 2,
        "mime_types": ["text/python", "text/x-ipython"],
        "display_name": "ruff",
    },
}
