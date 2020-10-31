import os


github_username = input("Please enter your github username: ")

grabDjango = "git clone https://github.com/" + github_username + "/django.git"

print("Attempting to clone django project to your local machine")
gotDjango = os.system(grabDjango)

navigateToDjango = "cd django/"
print("Attempting to navigate to Django folder")
inDjango = os.system(navigateToDjango)

print("Attempting to set virtual env")
setVirtEnv = "python3 -m venv ~/.virtualenvs/djangodev"
setEnv = os.system(setVirtEnv)

print("Attempting to activate virtual env")
activateVirtEnv = "source ~/.virtualenvs/djangodev/bin/activate"
activatedEnv = os.system(activateVirtEnv)

cwd = os.getcwd()

print("Attempting to install django and dependencies")
installRightHere = "python -m pip install -e" + cwd + "/django"
installed = os.system(installRightHere)

grabDependencies = "python -m pip install -r requirements/py3.txt "
gotDependencies = os.system(grabDependencies)

print("Attempting to run tests")
runTests = "./runtests.py"
ranTests = os.system(runTests)

