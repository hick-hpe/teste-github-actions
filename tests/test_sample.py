from main import func
from hello import hello_world

def test_hello_world(capsys):
    hello_world()
    captured = capsys.readouterr()
    assert captured.out == "Hello World\n"

def test_answer():
    assert func(3) == 4