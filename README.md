# Git Commands

git config --global user.name "name"
git config --global user.email "xyz@gmail.com"

git init                          create new git repository
git status                        gives information of a git repository
git add .                         add specific files to the staging area
git commit -m "Message"           commit changes from the staging area

git log                           list the commit
git log --oneline                 list one line of each commit

git branch                        view branch
gir branch <branch-name>          create a branch
git switch <branch-name>          switch branch
git switch -c <branch-name>       create branch and switch 
git checkout <branch-name>

git clone <url>                   clone a repo

git remote/git remote -v          view remote
git remote add <name> <url>       add a remote
git remote rename <old> <new>     rename remote
git remote remove <name>          delete remote

git push <remote> <branch>        push a branch to remote
git push <remote> <local-branch>:<remote-branch>
git push -u origin master




Create a file called .gitignore in the root of a repository. Inside the file, we can write patterns to tell Git which files and folders to ignore:
-> .DS_Store will ignore files named .DS_Store
-> folderName/ will ignore an entire directory
-> *.log will ignore any files with the .log extension

