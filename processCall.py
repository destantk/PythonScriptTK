import subprocess

cmd = "git --version"

return_data = subprocess.call(cmd, True)
if return_data == 0:
    print('returned data:', return_data)
else:
    print('returned data:', return_data)
