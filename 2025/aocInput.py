from pathlib import Path
import inspect

def dataInput():
    caller = Path(inspect.stack()[1].filename)
    txtFile = caller.with_suffix(".txt")

    return [line.strip() for line in txtFile.open() if line.strip()]
