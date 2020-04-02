gitTarget=$1
port=$2

#git clone $gitTarget

directory=${gitTarget##*/}
echo $directory
cd $directory
#npm install


echo "Starting server ..."
npm start $port &
wait
echo "Server started"

localHostUrl="http://localhost:"$port
python3 ../main.py $localHostUrl

read end
