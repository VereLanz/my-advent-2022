from pathlib import Path
import shutil
import sys
import webbrowser

from my_advent import YEAR


if __name__ == "__main__":
    if len(sys.args) < 2 or not isinstance(sys.args, int):
        raise TypeError(
            "The first command line argument has to be an "
            "integer representing the day of December for AoC."
        )
    # must be between 1 and 25
    day_nr = int(sys.args[1])
    here = Path(__file__).parent

    # copy day_template into f"day{day_nr}".py
    shutil.copy(
        here / "my_advent" / "day_template.py",
        here / "my_advent" / f"day{day_nr}.py",
    )

    # copy test_template into f"test_day{day_nr}".py
    with open(here / "tests" / "test_template.py", "r") as template:
        test_content = template.read()
        test_content.replace(".day_template", f".day{day_nr}")
        with open(here / "tests" / f"test_day{day_nr}.py", "w") as test_day:
            test_day.write(test_content)

    # open challenge of the day
    webbrowser.open(f"https://adventofcode.com/{YEAR}/day/{day_nr}")
