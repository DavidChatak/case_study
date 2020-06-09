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
    sudo yum install -y python3
    echo "done...."
else
    echo "There is already PYTHON3 installed...."
fi

pp="/usr/bin/python3"
# IFS=': ' read -r -a array <<< "$p"
ll=$(echo $PATH | grep $pp | wc -l )

if  [[ $ll != 0 ]]
    then
    echo "$pp in PATH"
    else
    echo "$pp is not in PATH, adding..."
    sleep 2
    echo "export PATH=$PATH:/usr/bin/python3" >> ~/.bashrc
    
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
fi
echo "phone_book.py running"
sleep 1


python3 phone.py
