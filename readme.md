# [Project Setup Guide](https://github.com/bakarilevy/python_manifest_hackathon)

---
### Important Links
- [Django Documentation](https://docs.djangoproject.com/en/dev/internals/contributing/new-contributors/)
- [Python Official Site](https://www.python.org/)
- [Git Source Code Management](https://git-scm.com/)
- [Visual Studio Code](https://code.visualstudio.com/)
- [Github Main Page](https://github.com/)
---
### Requirements
1. Download the Python Interpreter from the official site
2. Download Git Source Code Management
3. Download Visual Studio Code
4. Create a Github Account if you haven't already!
---
### Contributing to Django
1. Once all of the requirements have successfully been installed open up the command line of your choice,
You may use Powershell or Cmd on windows (powershell is highly recommended), or the Terminal on Mac. Once you're in the command line enter the
following command into the terminal to download the development version of the Django framework to your machine:
```
git clone https://github.com/YourGitHubName/django.git
```
2. After you have cloned the Django project, navigate into the folder by typing:
```
cd django/
```
Once you are in the folder for the Django project you will need to activate a virual environment by running the following command:
```
python3 -m venv ~/.virtualenvs/djangodev
```
A virtual environment is a workspace that keeps track of the dependencies for the project you are working with.
3. You can activate the virtual environment that you have created by entering the following command:
```
source ~/.virtualenvs/djangodev/bin/activate
```
4. Now you will need to install the django project you cloned inside of the virtual environment you just created, you can do that by running the following command:
```
python -m pip install -e /path/to/your/local/cloned/django
```
5. The next step is to grab all the dependencies django needs to run and have it installed in your virtual environment, that is accomplished by running this command:
```
python -m pip install -r requirements/py3.txt 
```
6. You can test everything to see if it works by running this command:
```
./runtests.py
```
7. Congratulations you are ready to dive into Django and get started!
---
### Quickstart
1. In a hurry? Download the python interpreter and git-scm from their main sites.
2. Create a github account if you haven't already
3. Download this repository by typing the following in the command line:
```
git clone https://github.com/bakarilevy/python_manifest_hackathon.git
```
4. Run the quickstart script!:
```
cd python_manifest_hackathon/

python3 quickstart.py
```