def readFile(filePath):
    with open(filePath, "r", encoding="utf-8") as file:
        return [line.strip() for line in file.readlines()]
