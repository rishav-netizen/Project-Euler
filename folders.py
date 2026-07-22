from pathlib import Path
baseProblem = 58
finalProblem = 60
for i in range(baseProblem, finalProblem + 1):
    folder = Path(f"problem{i}")
    folder.mkdir(exist_ok=True)

    (folder / "main.py").touch(exist_ok=True)
    (folder / "output.txt").touch(exist_ok=True)