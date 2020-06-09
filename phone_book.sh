#!/bin/bash
clear
sudo echo "welcome $USER"
if [ $? != 0 ] ;
    then
    echo "You are not member of sudoers, dude $whoami" 

fi
control=$(find . -name AccessLog.txt | wc -l)
if [ $control = 0 ]; then
echo "There is no file of AccessLog.txt "
echo "Creating AccessLog.txt ..... "
sleep 2
sudo touch AccessLog.txt
sudo chmod 777 AccessLog.txt
fi
num=$(cat AccessLog.txt | wc -l )
date=$( date )
sudo echo "$(($num+1)) $USER $date"  >> AccessLog.txt
control=$( sudo yum list installed python3 | wc -l )
if [ $control = 0 ]; then
    echo "There is NO Python3....."
    echo "installing Python3...."
    sleep 1
    #sudo yum install -y python3
    echo "done...."
    sleep 1
else
    echo "There is already PYTHON3 installed...."
fi
currentdir=$( pwd )
p=$( echo $PATH )
pp="/usr/bin/python3"
# IFS=': ' read -r -a array <<< "$p"
ll=$(echo $PATH | grep $pp | wc -l )

if  [[ $ll != 0 ]]
    then
    echo "$pp in PATH"
    else
    echo "$pp is not in PATH, adding..."
    sleep 1
    export PATH=$PATH:$pp
fi
# git control
git_control=$(sudo yum list installed git| wc -l)
if [ git_control > 0 ]
then 
echo "Git installed already"
else
sudo yum install git -y 
fi
#phone_book.py control

if [ -e phone.py ]
then
echo "phone.py exist"
else
echo "phone.py does not exist"
sudo wget https://github.com/DavidChatak/case_study/blob/master/phone.py
fi
echo "phone_book.py running"
sleep 1


python3 phone.py

# /home/ec2-user:/home/ec2-user/.vscode-server/bin/5763d909d5f12fe19f215cbfdd29a91c0fa9208a/bin:/home/ec2-user/.vscode-server/bin/5763d909d5f12fe19f215cbfdd29a91c0fa9208a/bin:/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/home/ec2-user/.local/bin:/home/ec2-user/bin:/usr/bin/python3
