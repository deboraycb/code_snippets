# 1. Create GitHub repo

- on github.com, go to your repositories, then click the green "New" button on the top right
- if you want to link an existing directory in your computer, give the same name to the GitHub repo
- in this example, the repository will be named TEST123

# 2. Create local directory to be linked with that repo

- if you are creating a new directory:

```
mkdir TEST123
echo "# testing" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:deboraycb/TEST123.git
git push -u origin main
```

- if you want to link and existing directory in your computer, cd into that directory, then:
```
cd TEST123
git init
git remote add origin git@github.com:deboraycb/TEST123.git
git branch -M main
git push -u origin main
```

# 3. To push your local file changes to GitHub

```
git add NAME_OF_FILE
git commit -m 'COMMIT MESSAGE'
git push
```

# 4. To pull changes from GitHub to your local dir

```
git pull
```

# TIPS

- Always do 'git pull' before you start working on your directory, so you are sure to be editing the most recent version on GitHub

- Always do git add/commit/push at the end of the day so you are sure that your changes are saved
