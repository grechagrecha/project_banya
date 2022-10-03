from settings import settings


def get_resolution() -> tuple:
    return settings.resolution


def get_framerate() -> int:
    return settings.framerate
