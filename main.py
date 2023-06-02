import json
with open("adventure.json", "r") as f:
    a = json.load(f)
def cmd_handler(gameloop, a):
    for command_name, command in a.items():
        bools = []
        for requirement_name, requirement in command["requirements"].items():
            bools.append(gameloop[requirement_name] == requirement)
        booltest = 0
        for i in bools:
            booltest += int(i)
        if booltest == len(bools):
            output = actioner(gameloop, a, command)
        else:
            output = gameloop
    return output
def actioner(gameloop, a, command):
    for action_name, action in command["replies"].items():
        if action_name == "reply":
            print(action)
        else:
            gameloop[action_name] = action
    return gameloop
def game_runner():
    gameloop = actioner({}, a, a["start"])
    while True:
        gameloop["keyword"] = input("type any command...\n")
        gameloop = cmd_handler(gameloop, a)
game_runner()