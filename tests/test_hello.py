import pytest

from nebula_realtime_autopilot.hello import say_hello


def test_say_hello():
    assert say_hello() == "Hello, World!"
