import typer
import sys
from typing import List


app = typer.Typer()

def count_bytes(file_path: str = None):
    if file_path:
        try:
            with open(file_path, 'rb') as file:
                content = file.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"Given file path {file_path} does not exists.")
    else:
        content = sys.stdin.read().encode()
    byte_count = len(content)
    return byte_count

def count_lines(file_path: str = None):
    if file_path:
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
        except FileNotFoundError:
            raise FileNotFoundError(f"Given file path {file_path} does not exists.")
    else:
        lines = sys.stdin.read().splitlines()
    line_count = len(lines)
    return line_count

def count_words(file_path: str = None):
    if file_path:
        try:
            with open(file_path, 'r') as file:
                content = file.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"Given file path {file_path} does not exists.")
    else:
        content = sys.stdin.read()
    words = content.split()
    word_count = len(words)
    return word_count

def count_chars(file_path: str = None):
    if file_path:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"Given file path {file_path} does not exists.")
    else:
        content = sys.stdin.read()
    char_count = len(content)
    return char_count

@app.command()
def main(
    files: List[str] = typer.Argument(None, help="The files to process"),
    c: bool = typer.Option(False, "--bytes", "-c", help="Print the byte counts"),
    l: bool = typer.Option(False, "--lines", "-l", help="Print the newline counts"),
    w: bool = typer.Option(False, "--words", "-w", help="Print the word counts"),
    m: bool = typer.Option(False, "--chars", "-m", help="Print the character counts"),
    version: bool = typer.Option(False, "--version", help="Show the version and exit")
):
    if version:
        typer.echo("ccwc version 0.1.0")
        raise typer.Exit()
    if not files:
        files = [None]
    for file in files:
        if c:
            byte_count = count_bytes(file)
            print(f"{byte_count:8} {file}")
        elif l:
            line_count = count_lines(file)
            print(f"{line_count:8} {file}")
        elif w:
            word_count = count_words(file)
            print(f"{word_count:8} {file}")
        elif m:
            char_count = count_chars(file)
            print(f"{char_count:8} {file}")
        else:
            line_count = count_lines(file)
            word_count = count_words(file)
            byte_count = count_bytes(file)
            print(f"{line_count:8} {word_count:8} {byte_count:8} {file}")

if __name__ == "__main__":
    app()
