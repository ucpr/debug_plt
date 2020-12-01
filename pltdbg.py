from logging import getLogger, StreamHandler, DEBUG, ERROR

logger = getLogger("debug_plt")
handler = StreamHandler()
handler.setLevel(ERROR)
logger.setLevel(ERROR)
logger.addHandler(handler)
logger.propagate = False

class DebugPlot:
    def __init__(self, logger, level=DEBUG):
        print(DEBUG)
        print("Call __init__\n")

    def __getattr__(self, name):
        print("Call __getattr__")
        print("name: {}".format(name))
        print("")

    def __setattr__(self, name, value):
        print("Call __setattr__")
        print("name: {}".format(name))
        print("value: {}".format(value))
        print("")

if __name__ == "__main__":
    test = Test(logger) # __init__が呼ばれる

    # __getattr__が呼ばれる
    # 存在しない属性でもOK
    test.aaa

    test.bbb = 1 # __setattr__が呼ばれる
