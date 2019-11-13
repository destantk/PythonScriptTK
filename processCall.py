import subprocess

file = open("gitCommand", "r")


def runShell(runnedScript):
    return subprocess.call(runnedScript, True)


for line in file:
    line = line.replace('\n', '')
    if not line.startswith('-') and len(line) > 1:
        return_data = runShell(line)
        if return_data == 0:
            print("OK", line)
        else:
            print("NO", line)

file.close()
