# Git Commands

```bash
git config --global user.name "name"
git config --global user.email "xyz@gmail.com"
```
#

create new git repository
```bash
git init   
```
gives information of a git repository
```bash
git status  
```
 add specific files to the staging area
```bash
git add . 
```
 commit changes from the staging area
```bash
git commit -m "Message"  
```

 list the commit
```bash
git log 
```
 list one line of each commit
```bash
git log --oneline  
```

                          
               






                      
         
         
       

#
view branch
```bash
git branch 
```
create a branch
```bash
gir branch <branch-name> 
```
switch branch
```bash
git switch <branch-name>
git checkout <branch-name>
```
create branch and switch 
```bash
git switch -c <branch-name>
```
#




clone a repo
```bash
git clone <url>
```
#
          
     
     
          
view remote    
```bash
git remote/git remote -v
```
add a remote
```bash
git remote add <name> <url> 
```
rename remote
```bash
git remote rename <old> <new>
```
delete remote
```bash
git remote remove <name>
```
#


push a branch to remote
```bash
git push <remote> <branch>        
git push <remote> <local-branch>:<remote-branch>
```
#



push a branch to remote
```bash
git push <remote> <branch>       
git push <remote> <local-branch>:<remote-branch>
```
add upstream
```bash
git push -u origin master
```
#


##.gitignore
Create a file called .gitignore in the root of a repository. Inside the file, we can write patterns to tell Git which files and folders to ignore:
- -> .DS_Store will ignore files named .DS_Store
- -> folderName/ will ignore an entire directory
- -> *.log will ignore any files with the .log extension

