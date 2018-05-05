import unittest

from ..auxiliary import VAR
from ..utils import Logger

__all__ = ["TestCase"]


class TestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.log = Logger.get_logger(self.__class__.__name__)

        self.ad = getattr(VAR, "ad")
        setattr(self.ad,"log",self.log)
