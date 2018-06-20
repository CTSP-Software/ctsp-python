#! /bin/bash 

# asking for root access
[ $UID != 0 ] && exec sudo bash "$0" "$@"

# installing dependencies
apt install -y python3
apt install -y python3-dev
apt install -y python3-venv
apt install -y python3-pip
apt install -y mysql-client
apt install -y mysql-server
apt install -y libmysqlclient-dev
apt install -y expect

# configuring mysql user, and correcting a plugin problem that has been introduced in version 17.10
# if you're not using ubuntu 17.10, this will probably not change any configuration
echo -en "\n[root] root password for mysql:"
read -s rpw

# making needed changes to mysql
mysql -u root -p${rpw} -e "create database ctsp;create user 'ctsp'@'localhost' identified by '123456';grant all on ctsp.* to 'ctsp'@'localhost';update mysql.user set plugin='' where User='ctsp';flush privileges"

# creating the virtual env
python3 -m venv ../venv

# activating virtual environment
source ../venv/bin/activate

# installing needed packages
pip3 install -U wheel 
pip3 install -U pytz
pip3 install -U pylint 
pip3 install -U autopep8 
pip3 install -U django 
pip3 install -U mysqlclient

# makemigrations
python ../project/manage.py makemigrations

# migrate 
python ../project/manage.py migrate

# ask if want to run up the server
echo -en "\nDo you wish to run the server? Type 'yes' to run, or 'no' to cancel:"
read answer

if [ $answer == "yes" ]
then
    python ../project/manage.py runserver
fi
