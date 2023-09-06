import sys


def get_time(minutes: int) -> str:
    return f"{str(minutes//60).zfill(2)}:{str(minutes%60).zfill(2)}"


def get_progress(percents: int) -> str:
    return f"{str(percents).rjust(2)}%"


filename = sys.argv[1]

with open(filename, "r", encoding="utf-8") as file:
    data = file.readlines()

with open(filename, "w", encoding="utf-8") as file:
    for row in data:
        if not row.startswith("M73"):
            file.write(row)
            continue
        # https://reprap.org/wiki/G-code#M73:_Set.2FGet_build_percentage
        row = row.replace("D", "C").replace("S", "R").replace("Q", "P")
        args = {m[0]: int(m[1:]) for m in row.split()[1:]}  #  Get command arguments
        if "C" in args:
            #  Time to change/pause/user interaction
            minutes = args["C"]
            new_row = f"M117 {get_time(minutes)} to pause\n"
        else:
            #  Time until printing is done and progress done
            progress, minutes = args["P"], args["R"]
            new_row = f"M117 {get_time(minutes)} left / {get_progress(progress)} done\n"
        file.write(new_row)
