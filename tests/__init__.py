import pytest


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    class EnsureThat(object):

        @staticmethod
        def is_same(text1: str, text2: str):
            if not text1 == text2:
                raise AssertionError(f"{text1} != {text2}")

        @staticmethod
        def is_true(value):
            if not bool(value):
                raise AssertionError(f"boolean({value}) != True")

        @staticmethod
        def text_in(text1: str, text2: str):
            if not (text1 in text2 or text2 in text1):
                error = f""""
                {text1} not in {text2}
                        OR
                {text2} not in {text1}
                """
                raise AssertionError(error)
