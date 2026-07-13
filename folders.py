from pathlib import Path
baseProblem = 51
finalProblem = 55
for i in range(baseProblem, finalProblem + 1):
    folder = Path(f"problem{i}")
    folder.mkdir(exist_ok=True)

    (folder / "main.py").touch(exist_ok=True)