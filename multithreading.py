from threading import Thread
from threading import Lock


class LockingCounter:
    def __init__(self):
        self.lock = Lock()
        self.count = 0

    def increment(self, offset):
        with self.lock:
            self.count += offset


def worker(sensor_index, count, cnt):
    for _ in range(count):
        # Read from the sensor
        ...
        cnt.increment(1)


how_many = 10**5
counter = LockingCounter()
threads = []
for i in range(5):
    thread = Thread(target=worker, args=(i, how_many, counter))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

expected = how_many * 5
found = counter.count
print(f'Counter should be {expected}, got {found}')


def test():
    pass


if __name__ == '__main__':
    print("Start")
    test()
    print("Finished")
