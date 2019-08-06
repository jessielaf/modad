from modad.parser import Config


class _State:
    temp_folders = []
    config: Config


state = _State()
