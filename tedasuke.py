class tedasuke:
    def __init__(self, instance, logger, level=DEBUG):
        self._instance = instance
        self._level = level

    def __getattr__(self, name):
#        if self._level == logger.get
        return getattr(self._instance, name)

    def _cb(self):
        pass


if __name__ == "__main__":
    test = tedasuke("abs", logger)

    print(test.split("b"))
