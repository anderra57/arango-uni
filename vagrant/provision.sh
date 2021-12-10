#!/bin/bash

SEP="----------------"
echo -e "$SEP\nStarting provisioning..."

# set environment vars
export ARANGO_ROOT_PASSWORD=passwd 
export DEBIAN_FRONTEND=noninteractive

# define arangodb password for unattended installation
echo arangodb3 arangodb3/password password $ARANGO_ROOT_PASSWORD | debconf-set-selections
echo arangodb3 arangodb3/password_again password $ARANGO_ROOT_PASSWORD | debconf-set-selections

# add arangodb repository
echo -e "$SEP\nAdding ArangoDB repository..."
sudo -E apt-get -qy update &> /dev/null
sudo -E apt-get -qy install gnupg &> /dev/null
sudo -E apt-get -qy install curl &> /dev/null
curl -OL https://download.arangodb.com/arangodb38/DEBIAN/Release.key &> /dev/null
sudo -E apt-key add - < Release.key &> /dev/null
echo 'deb https://download.arangodb.com/arangodb38/DEBIAN/ /' | sudo tee /etc/apt/sources.list.d/arangodb.list &> /dev/null
echo -e "ArangoDB repository added!"

# install arangodb
echo -e "$SEP\nInstalling ArangoDB..."
sudo -E apt-get -yq update &> /dev/null
sudo -E apt-get -yq install apt-transport-https &> /dev/null
sudo -E apt-get -y install arangodb3 &> /dev/null
echo -e "ArangoDB installed!"

# start arangodb
echo -e "$SEP\nEnabling ArangoDB..."
sudo systemctl start arangodb3 &> /dev/null
sudo systemctl enable arangodb3 &> /dev/null
echo -e "ArangoDB enabled!"

# install python flask
echo -e "$SEP\nInstalling Python and Flask modules..."
sudo -E apt-get -qy update &> /dev/null
sudo -E apt-get -qy install python3 python3-pip &> /dev/null
pip install -r /app/requirements.txt &> /dev/null
echo -e "Python and Flask modules installed!"

echo -e "$SEP\n\nProvisioning complete!"