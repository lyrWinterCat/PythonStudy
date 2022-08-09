# ThreadEx

from time import*

#from threading import*
from threading import Thread

# run()
class MyThread(Thread):
    def __init__(self,msg):
        Thread.__init__(self)
        #부모클래스의 생성자를 반드시 호출해주어야함
        # => 인스턴스를 생성했을때 run()이 자동적으로
        # 수행됨 !
        self.msg=msg

    def run(self):
        #수행명령문
        while True:
            sleep(1)
            print(self.msg)

#main()
for msg in ['you','need','python']:
    t = MyThread(msg)
    t.setDaemon(True)
    t.start()

for i in range(100):
    sleep(0.1)
    print(i)
