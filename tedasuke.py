from logging import DEBUG


class tedasuke:
    def __init__(self, instance, logger, level=DEBUG):
        self._instance = instance
        self._passing_level = level
        self._level = logger.getEffectiveLevel()

    def __getattr__(self, name):
        # https://github.com/python/cpython/blob/master/Lib/logging/handlers.py#L722
        if self._passing_level < self._level:
            return self._cb
        return getattr(self._instance, name)

    def _cb(self):
        pass
