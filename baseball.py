import sys
import os
import re

class Player:
    def __init__(self, fName, lName, totalAtBats, hits):
        self.first = fName
        self.last = lName
        self.totalAtBats = int(totalAtBats)
        self.hits = int(hits)

    def __str__(self):
        return f"{self.first} {self.last}: {self.average():.3f}"

    def average(self):
        return round(self.hits / self.totalAtBats, 3) if self.totalAtBats > 0 else 0.0

# Regex pattern to match player stats
player_regex = re.compile(r"([A-Z][a-z]+) ([A-Z][a-z]+) batted (\d+) times with (\d+) hits and (\d+) runs")

# Ensure a filename is provided
if len(sys.argv) < 2:
    sys.exit(f"Usage: {sys.argv[0]} <filename>")

filename = sys.argv[1]

# Check if file exists before attempting to open
if not os.path.exists(filename):
    sys.exit(f"Error: File '{filename}' not found")

players = {}

with open(filename) as f:
    for line in f:
        match = player_regex.match(line)
        if match:
            first, last, at_bats, hits = match.group(1), match.group(2), int(match.group(3)), int(match.group(4))
            key = (first, last)

            if key in players:
                players[key].totalAtBats += at_bats
                players[key].hits += hits
            else:
                players[key] = Player(first, last, at_bats, hits)

# Sort players by batting average in descending order
sorted_players = sorted(players.values(), key=lambda p: p.average(), reverse=True)

for player in sorted_players:
    print(player)