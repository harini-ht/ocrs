# ocrs
online course reservation system - A Django Based Web Portal 

# Installation 

- Step 1 : Make sure that you're already installed [Python 3.x](https://www.python.org/downloads/) on your system.
- Step 2 : Open your terminal and then type

```cmd
mkdir ocrs
cd ocrs
```

- Step 3: Type following commands to initialize the git and set remote origin (for updated package in future).

```cmd
git init
git remote add origin https://github.com/harini-ht/ocrs.git
```

- Step 4 : Clone the repo by using following command.

```cmd
git branch -M main
git pull origin main
```

> DANGER :
>
> 1. Don't use `git push` command on the main branch.
> 2. Use `git push origin dev` or create your own branch to work on.

- Step 5 : Type in the terminal the following commands to install the dependencies and start the server
```cmd
pip install -r requirements.txt
python manage.py runserver 
```

# Update your changes

```cmd
git add .
git commit -m "<COMMIT-MESSAGE>"
git push origin dev
```


