from multiprocessing import Process
import sys

def f(name):
    print 'hello', name

if __name__ == '__main__':
    p = Process(target=f, args=('world',))
    p.start()
    p.join()
    # make sure all output has been processed before we exit
    sys.stdout.flush()
