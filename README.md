## Automated repository creation

#### Necessary software 
* Selenium
* Cromedrive

#### Download
Run in your terminal:
```
cd
git clone https://github.com/nestoregon/my_commands.git
```
This will install the repository in the home/username directory

#### Setup
Your .bashrc file needs to be updated. This file is executed each time a new terminal is opened.
To edit the file:
```
nano ~/.bashrc
```
Add the following lines at the end of the .bashrc file

```
source ~/my_commands/.repo_create.sh
source ~/my_commands/.repo_remove.sh
```

Check ALL the files and replace "nestoregon" with your corresponding GitHub or Linux username

While using the terminal you can now type:
* ```repo_create file_name``` to create a repository with that name
* ```repo_remove file_name``` to remove a repository with that name

** NOTE: At the time of this post ALL Chrome tabs needed to be closed for the scripts to work. It may also be necessary to log into your GitHub account for the first time.