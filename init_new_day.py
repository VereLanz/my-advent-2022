from pathlib import Path
import shutil
import sys
import webbrowser

from my_advent import YEAR

README_DAILY_TEMPLATE = \
"""### *title*
[code &#8614;](https://github.com/VereLanz/my-advent-{year}/blob/main/my_advent/day{day_nr}.py)
### Part One
-

### Part Two
-"""


if __name__ == "__main__":
    if len(sys.argv) < 2 or not sys.argv[1].isdigit():
        raise TypeError(
            "The first command line argument has to be an "
            "integer representing the day of December for AoC."
        )
    # must be between 1 and 25 (not checked)
    day_nr = int(sys.argv[1])
    here = Path(__file__).parent

    # copy day_template into f"day{day_nr}".py
    shutil.copy(
        here / "my_advent" / "day_template.py",
        here / "my_advent" / f"day{day_nr}.py",
    )

    # copy test_template into f"test_day{day_nr}".py
    with open(here / "tests" / "test_template.py", "r") as template:
        test_content = template.read()
        test_content = test_content.replace(".day_template", f".day{day_nr}")
        with open(here / "tests" / f"test_day{day_nr}.py", "w") as test_day:
            test_day.write(test_content)

    # edit readme.me to add daily text template
    day_readme = README_DAILY_TEMPLATE.format(year=YEAR, day_nr=day_nr)
    with open(here / "README.md", "r+") as readme:
        readme_content = readme.readlines()
        try:
            day_idx = readme_content.index(f"## Day {day_nr}\n")  # should all exist for 1 to 25
            readme_content.insert(day_idx + 1, day_readme)
        except:
            # if for some reason key was not found, rewrite readme as it was
            pass
        # new text will always be longer than or the same as before, so no truncate needed
        readme.seek(0)
        readme.writelines(readme_content)

    # open challenge of the day
    webbrowser.open(f"https://adventofcode.com/{YEAR}/day/{day_nr}")
