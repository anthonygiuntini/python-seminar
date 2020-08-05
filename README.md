# python-seminar
Welcome to the Git repository for Schuyler's python seminar. Content will be added to this as we go. Feel free to put your own code in a folder labelled with your name in the "Student Code" directory. 

## Get Started with Git
Git is a tool for verisioning (keeping track of changes) and collaborating with code files. This is a git repository, which is a "bucket" for all of the files that git keeps track of.


To clone this use this command: `git clone https://github.com/anthonygiuntini/python-seminar.git`
Cloning creates a copy of the repository in the folder that you were in when you ran the command

To update your local repository (the one on your computer, not the server), use the command `git pull` while your active directory (the folder the command prompt is in) is the original repository folder i.e. python-seminar. This will "pull" the changes from the server to your computer.

## Basic steps
1. You should have already installed git (based on intro email), which is primarily a command line tool.
2. Open the bash command line  
        - on windows computers, navigate to the folder where you want the files stored, right click, and select "Git bash here." This should open up a command line. 
        - on mac computers go to applications>utilities and open the "Terminal" application. Once in the terminal: use the `cd <path>` command to change the active directory to the folder that you want. Replace `<path>` with the path to the folder. For example say I want to point to my documents folder, the path would be `/Users/agiuntini/Documents` (agiuntini is my username) Each name in between the forward slashes represents a folder.
3. Once in the working directory clone the repository with:  `git clone https://github.com/anthonygiuntini/python-seminar.git` - This should download all of the files. You only need to do this once.
4. To update the files on your computer use: `git pull`

### Note: do not add any files to the folder that is created by git (`python-seminar`). When you `pull` your files might be overwritten, or you won't be able to `pull`. 

### We'll discuss git in more depth later. As always, let me know if you have any questions.
