import subprocess

def test_help():
    result = subprocess.run(['ccwc', '--help'], capture_output=True, text=True)
    assert "Usage" in result.stdout

def test_version():
    result = subprocess.run(['ccwc', '--version'], capture_output=True, text=True)
    assert "ccwc version 0.1.0" in result.stdout

def test_byte_count():
    result = subprocess.run(['ccwc', '--bytes', 'test.txt'], capture_output=True, text=True)
    assert "342190" in result.stdout

def test_line_count():
    result = subprocess.run(['ccwc', '--lines', 'test.txt'], capture_output=True, text=True)
    assert "7145" in result.stdout

def test_word_count():
    result = subprocess.run(['ccwc', '--words', 'test.txt'], capture_output=True, text=True)
    assert "58164" in result.stdout

def test_char_count():
    result = subprocess.run(['ccwc', '--chars', 'test.txt'], capture_output=True, text=True)
    assert "332147" in result.stdout

def test_default():
    result = subprocess.run(['ccwc', 'test.txt'], capture_output=True, text=True)
    assert "7145" in result.stdout
    assert "58164" in result.stdout
    assert "342190" in result.stdout
