import sys

sys.path.append('~/api_python')
from src import app

def test_bananinha():
    assert 42 == app.bananinnha()