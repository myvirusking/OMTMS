# OMTMS
ONLINE MOVIE TICKET MANAGEMENT SYSTEM

**********Confuguration Git Clone In Linux(like Ubantu)****************

Install Git with Apt :
sudo apt-get update
sudo apt-get install git

Set Up Git config --global:
git config --global user.name "Your Name"
git config --global user.email "youremail@domain.com"
git config --global http.sslcainfo=/bin/curl-ca-bundle.crt
git config --global http.sslverify=false
git config --global --unset http.proxy

Git command:
make one file using cat > readme.txt
git init
git add readme.txt
git commit -m "first commit"
git remote add origin yourHTTPSreprolink (ex. https://github.com/foldername/gitreproname.git)
git push -u origin master