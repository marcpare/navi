import re

regex = r"^([a-z!\-]+)\s(.+)"

print("% git, zsh")

with open("ohmyzsh.txt") as f:
    for line in f:
        match = re.match(regex, line)
        # print(match.group(0)) # the full line

        print(f"# Command {match.group(2)}")
        print(match.group(1))
