reindent ./main-opengl.py
python ./main-opengl.py &
pid=`ps | grep "Python" | head -n 1 | awk '{print $1}'`
sleep 0.5
osascript ./focus.applescript $pid
