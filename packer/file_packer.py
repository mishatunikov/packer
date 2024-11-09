import time
import pandas as pd

from multiprocessing.pool import Pool
from random import randint

from collections import defaultdict, deque

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))


class FilePacker:
    def __init__(self, data: dict) -> None:
        self.data = pd.DataFrame(data)

    def create_excel(self):
        self.data.to_excel('data.xlsx', index=False)

    def create_csv(self):
        self.data.to_csv('data.csv', index=False)

    def create_txt(self):
        pass

    def create_files(self):
        pass
