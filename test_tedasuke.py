from logging import getLogger, DEBUG, INFO
import pytest

from tedasuke import tedasuke


@pytest.fixture
def logger():
    l = getLogger(__name__)
    return l


def test_tedasuke(logger):
    logger.setLevel(DEBUG)
    t = tedasuke("str ing", logger, level=DEBUG)
    result = t.split()
    want = ["str", "ing"]
    assert result == want

    logger.setLevel(INFO)
    t = tedasuke("str ing", logger, level=DEBUG)
    result = t.split()
    want = None
    assert result == want
