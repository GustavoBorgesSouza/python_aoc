import sys

sys.path.append('~/api_python')
from src import app

# def test_bananinha():
#     assert 42 == app.bananinnha()

def test_solve():
    firstDay = app.Solve(fileName="src/day1_example.txt")
    assert 294 == firstDay.solve()

def test_solve_only_digits():
    firstDay = app.Solve(fileName="src/day1_example.txt")
    assert 223 == firstDay.solve(includeSpelled=False)