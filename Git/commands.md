# Important commands 

>In most of this examples it can be used a dot
> "." meaning incuding all files

+ `git clone HTTPS_name`

    + Create a folder in your local machine

+ `git init`
    
    + Transform a folder in git folder

+ `git diff`

    + Show all changes

+ `git diff --staged`

    + Changes in staged files

+ `git diff origin/main`

    + Show all changes that git pull has.

+ `git log`

    + Show all last versions and updates on repo.

+ `git log --oneline`

    + Show all last versions in one line.

+ `git fetch`

    + Show all changes that git pull has. (but must use git diff to see it).    

+ `git pull HTTPS_name`

    + Updates the code with the latest version.

+ `git status`

    + Show branch version; show untracked files.

+ `git add name_file`

    + Add file but must be commited

+ `git commit file_name -m "Commit message"`

    + Commit all changes to a file with a brief summary

+ `git push origin branch_name`

    + Push all commits to github.

+ `git restore --source=hexadecimal_code file_name`

    + Restore the version hexadecimal commit version in the file_name (you can use . for all files commited in this commit).

+ `git restore --staged files_name`

    + Move file to staged changes for changes.

+ `git checkout -b branch_name`

    + Creates a new branch and switch it.

+ `git switch branch_name`

    + Switch between branches. 

+ `git branch branch_name`

    + Creates a branch but don't switch.

+ `git branch`

    + Show all branches

+ `git merge mergining_branch`

    + Merge branches.

+ `git config --global user.email "git_email"`

    + Prepare your machine with your git account

+ `git config --global user.name "git_name"`

    + Prepare your machine with your git account