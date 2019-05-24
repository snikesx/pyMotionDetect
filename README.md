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
`python pyMotionDetect.py -d /dev/video0 -c pyMotionDetec.config`  
`./pyMotionDetect`

вместо /dev/video0 можно использовать другие камеры или видео файлы
в некоторых *nix системах для чтения с камеры нужны права, поэтому необходимо запускать приложение с соответствующими параметрами


По умолчанию видео сохраняется в папку cam, если у вас ее нет, создайте, укажите права на запись
