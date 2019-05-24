Welcome to the pyMotionDetect

### Зависимости: 
Python 2.7

**OpenCV**  
`apt-get install python-opencv`

**Numpy**  
`pip install numpy`

**YAML**  
`apt-get install python-yaml`  

**argparse**  
`apt-get install python-argparse`



### Запуск
`python pyMotionDetect.py`  
`python pyMotionDetect.py -i /dev/video0 -c pyMotionDetec.config`  
`python pyMotionDetect.py -d -i /dev/video0 -c pyMotionDetec.config`  
  
`./pyMotionDetect`  
`./pyMotionDetect -d`  
`./pyMotionDetect -d -i 0`  

**arguments:**  
  -i --input - устровство ввода видео для linux 0 или /dev/video0, для windows - 0  
  -c --config - применить альтернативный конфиг  
  -d --deamon - запуск в режиме демона (только для Linux)  
  

вместо /dev/video0 можно использовать другие камеры или видео файлы
в некоторых *nix системах для чтения с камеры нужны права, поэтому необходимо запускать приложение с соответствующими параметрами


По умолчанию видео сохраняется в папку cam, если у вас ее нет, создайте, укажите права на запись
