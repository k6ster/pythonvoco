from pathlib import Path

with open("logi.txt", "a", encoding="utf-8") as fail:
    fail.write("Uus sissekanne\n")
print(Path("logi.txt").read_text(encoding="utf-8"))
