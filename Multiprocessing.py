from multiprocessing import Process
import time


def print_a():
    for i in range(500):
        print("Process A!")
        time.sleep(1)


def print_b():
    for i in range(500):
        print("Process B!")
        time.sleep(2)


if __name__ == '__main__':

    p_a = Process(target=print_a)
    p_b = Process(target=print_b)
    count = 0
    while True:
        count = count + 1
        if count == 100000000:
            count = 0
        if count == 50:
            p_a.start()
        if count == 70:
            p_b.start()
        time.sleep(0.1)
    p_a.join()
    p_b.join()
