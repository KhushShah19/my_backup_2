**Git basic commands**

< br > == next line <br>
BLOB (OB = object) represent files in git <br>
Tree (object) represent dicrectory <br><br>

- git command_name -h ==> help us with that command <br>
git help command_name ==> open a browser and give detail explanation/help
> ## git init -h
---
- git inti ==> to start/initialize git in that file/repository <br> 
there is a new .git repository, it holds ypur data related to get. <br>
this .git is actually a hidden sub directory of actual folder. <br> 
rm -rf .git ==> to remove.git file 
> git init <br> 
> & Initialized empty Git repository in  C:/VS_Code_folder/.git/ <br>
---
- git add file1_name file2_name ==> adding single/multiple files <br>
git add . ==> adds all the file in staging area <br>
these files are not saved yet, it just means they're ready for commit.
> git add file1_name file2_name <br>
> & Changes to be committed : (use "git rm --cached <file>..." to unstage) <br>
> & new file : file1_name file2_name
---
- git commit -m "helful message" ==> saving the changes (taking snapshots) <br>
git coomit ==> if your message is bigger (try to avoid it) <br>
-m == message = keep it to point, anyone can read it. <br>
all the codes are saved after commit statement 
> git commit -m "added something" <br>
> & [master (root-commit) 0756fcc] added print statement  <br>
> & 1 file changed, 5 insertions(+) <br>
> & create mode 100644 LG_01.py <br>
---
- git commit -a -m 'sweet message' ==> to commit without adding it <br>
git coomit -am 'message' ==> a for all file and m for message <br>
> git commit -a -m 'special message added' <br>
> & [master 35ac678] special message added <br>
> & 1 file changed, 1 insertion(+), 1 deletion(-)
---
- git commit --amend -m 'short message' ==> to modify the already existing commit <br>
it makes the new commit with new id (maybe even message) in place of old one. <br>
Date and time will be of old commit (remain same) but commit id is changed.
> git commit --amend -m 'to replace old commit'
---
- git status ==> to know the status of your working directory <br>
this can tell which file is to commit and which to add. <br>
git status -s ==> for shortten the status
> git status -s <br>
> & M file_name 
---
- git ls-files ==> files present in staging area <br>
> git ls-files <br>
>  & file1_name
---
- rm file2_name ==> to remove/delete this file <br>
this is not a git command and this change is neither add nor commited. <br>
to save it, we need to add this file then commit it.
> rm file2_name <br>
> &
---
- git rm file2_name ==> to remove this from git and system <br>
no need to add or commit any thing. rm = remove
> git rm file2_name <br>
> & 
---
- git mv file1_name file_name ==> to remane/move the file <br>
after the rename/move, the file is automatically added but not commited.
> git mv file1_name file_name <br>
> &
---
- gitignore ==> add this file to your root directory <br>
add file in it, which should be ignored by Git <br>
even this file needs to be added then commited. 
---
- git diff ==> compare local area vs staged area <br>
git diff --staged ==> compare staged vs last commited
> git diff --staged <br>
> &
---
- git log ==> shows all the commit history <br>
press q => to exit the log entires <br>
git log --oneline ==> shows all the commit history in oneline. <br>
git log --oneline --reverse ==> to show lastest in last (acc order)
> git log --oneline <br>
> & 2979bf7 (HEAD -> master) added ignored file <br>
> & 35ac678 another print statement
---
- git show ==> show the actual code changes
> git show cbe1249b140dad24b2c35b15cc7e26a6f02d2277 (commit_id)
---
- git restore file_name ==> reverse the changes you have made. <br>
git restore --staged file_name ==> reverse the changes in staged area <br>
git restore --scorce=head~1 file_name.py ==> bring back the pervious version <br>
it also means it copy the last snapshot and give it back to you.
> git restore --staged file_name
---
- git clean -f ==> it delete that file from git
for more info go to git clean -h
> git clean -h
---
- git clone url ==> copy the code present in git remote (online github)
> git clone git_user @git_server.com:demo.git
---
- git push ==> put your code on remote repository (online github) <br>
why we use origin and why only master??
> git push origin master
---
- git pull ==> to synchronize your local repository with the remote one. <br>
can't push the code if code don't have the lastest commit in remote repository 
> git pull
---
