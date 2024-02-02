import sys

sys.path.append('~/api_python')
from src import app

def test_bananinha():
    assert 42 == app.bananinnha()

def test_estrelinha():
    assert 281 == app.estrelinha(
        "src/day1_example.txt"
    )