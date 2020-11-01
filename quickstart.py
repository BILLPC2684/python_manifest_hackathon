import os

def runWin(djangoCommand):
    print("Windows operating system detected")

    print("Attempting to clone django project to your local machine")
    gotDjango = os.system(djangoCommand)

    navigateToDjango = "cd django/"
    print("Attempting to navigate to Django folder")
    inDjango = os.system(navigateToDjango)

    print("Attempting to set virtual env")
    setVirtEnv = "py -m venv %HOMEPATH%\.virtualenvs\djangodev"
    setEnv = os.system(setVirtEnv)

    print("Attempting to activate virtual env")
    activateVirtEnv = "%HOMEPATH%\.virtualenvs\djangodev\Scripts\activate.bat"
    activatedEnv = os.system(activateVirtEnv)

    cwd = os.getcwd()

    print("Attempting to install django and dependencies")
    installRightHere = "py -m pip install -e " + cwd + "\django"
    installed = os.system(installRightHere)

    grabDependencies = "py -m pip install -r requirements\py3.txt"
    gotDependencies = os.system(grabDependencies)

    print("Attempting to run tests")
    runTests = "py runtests.py"
    ranTests = os.system(runTests)



def runUni(djangoCommand):
    print("Unix based operating system detected")

    print("Attempting to clone django project to your local machine")
    gotDjango = os.system(djangoCommand)

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



def main():
    github_username = input("please enter your github username: ")
    grabDjango = "git clone --depth 1 https://github.com/" + github_username + "/django.git"
    if os.name == 'nt':
        runWin(grabDjango)
    else:
        runUni(grabDjango)


if __name__ == "__main__":
    main()
