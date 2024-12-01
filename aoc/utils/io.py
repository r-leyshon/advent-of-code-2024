"""Utilities for loading puzzles inputs."""

def load_input(pth) -> str:
    if not pth.suffix == ".txt":
        raise ValueError("Input must be a txt file")
    with open(pth, "r") as f:
        lines = f.read()
        lines = lines.splitlines()
    return lines
