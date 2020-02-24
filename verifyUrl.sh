# git clone https://github.com/xileftenurb/polymtl-inf8007-site-exemple
gitTarget=$1
port=$2

cd polymtl-inf8007-site-exemple
# npm install


echo "Starting server ..."
npm start $port &
sleep 3
echo "Server started"

localHostUrl="http://localhost:3000"
python3 ../main.py $localHostUrl

read end
