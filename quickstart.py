import os


github_username = input("Please enter your github username: ")
cm1 = "git clone https://github.com/" + github_username + "/django.git"
print("Attempting to clone django project to your local machine")
res1 = os.system(cm1)
cm2 = "cd django/"
print("Attempting to navigate to Django folder")
res2 = os.system(cm2)
cm3 = "python3 -m venv ~/.virtualenvs/djangodev"
cm4 = "source ~/.virtualenvs/djangodev/bin/activate"
cwd = os.getcwd()
cm5 = "python -m pip install -e" + cwd + "/django"
cm6 = "python -m pip install -r requirements/py3.txt "
cm7 = "python runtests.py"
print(cm5)
