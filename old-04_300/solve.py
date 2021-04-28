import hashlib
import threading

hashed = '291cb63aa6963ed2641c7c378023f8ac7cb76b1b'

def first():
    print('thread_1 start')
    for i in range(10000000, 20000000):
        data = str(i) + 'salt_for_you'
        answer = data
        for _ in range(500):
            m = hashlib.sha1()
            m.update(data.encode('utf-8'))
            h = m.hexdigest()
            data = h
        if data is hashed:
            print(answer)
            break

def second():
    print('thread_2 start')
    for i in range(20000000, 30000000):
        data = str(i) + 'salt_for_you'
        answer = data
        for _ in range(500):
            m = hashlib.sha1()
            m.update(data.encode('utf-8'))
            h = m.hexdigest()
            data = h
        if data is hashed:
            print(answer)
            break

def third():
    print('thread_3 start')
    for i in range(30000000, 40000000):
        data = str(i) + 'salt_for_you'
        answer = data
        for _ in range(500):
            m = hashlib.sha1()
            m.update(data.encode('utf-8'))
            h = m.hexdigest()
            data = h
        if data is hashed:
            print(answer)
            break

def forth():
    print('thread_4 start')
    for i in range(40000000, 50000000):
        data = str(i) + 'salt_for_you'
        answer = data
        for _ in range(500):
            m = hashlib.sha1()
            m.update(data.encode('utf-8'))
            h = m.hexdigest()
            data = h
        if data is hashed:
            print(answer)
            break

def fifth():
    print('thread_5 start')
    for i in range(50000000, 60000000):
        data = str(i) + 'salt_for_you'
        answer = data
        for _ in range(500):
            m = hashlib.sha1()
            m.update(data.encode('utf-8'))
            h = m.hexdigest()
            data = h
        if data is hashed:
            print(answer)
            break

def sixth():
    print('thread_6 start')
    for i in range(60000000, 70000000):
        data = str(i) + 'salt_for_you'
        answer = data
        for _ in range(500):
            m = hashlib.sha1()
            m.update(data.encode('utf-8'))
            h = m.hexdigest()
            data = h
        if data is hashed:
            print(answer)
            break

def seventh():
    print('thread_7 start')
    for i in range(70000000, 80000000):
        data = str(i) + 'salt_for_you'
        answer = data
        for _ in range(500):
            m = hashlib.sha1()
            m.update(data.encode('utf-8'))
            h = m.hexdigest()
            data = h
        if data is hashed:
            print(answer)
            break

def eighth():
    print('thread_8 start')
    for i in range(80000000, 90000000):
        data = str(i) + 'salt_for_you'
        answer = data
        for _ in range(500):
            m = hashlib.sha1()
            m.update(data.encode('utf-8'))
            h = m.hexdigest()
            data = h
        if data is hashed:
            print(answer)
            break

def nineth():
    print('thread_9 start')
    for i in range(90000000, 100000000):
        data = str(i) + 'salt_for_you'
        answer = data
        for _ in range(500):
            m = hashlib.sha1()
            m.update(data.encode('utf-8'))
            h = m.hexdigest()
            data = h
        if data is hashed:
            print(answer)
            break

thread_1 = threading.Thread(target=first)
thread_2 = threading.Thread(target=second)
thread_3 = threading.Thread(target=third)
thread_4 = threading.Thread(target=forth)
thread_5 = threading.Thread(target=fifth)
thread_6 = threading.Thread(target=sixth)
thread_7 = threading.Thread(target=seventh)
thread_8 = threading.Thread(target=eighth)
thread_9 = threading.Thread(target=nineth)

thread_1.start()
thread_2.start()
thread_3.start()
thread_4.start()
thread_5.start()
thread_6.start()
thread_7.start()
thread_8.start()
thread_9.start()

thread_1.join()
thread_2.join()
thread_3.join()
thread_4.join()
thread_5.join()
thread_6.join()
thread_7.join()
thread_8.join()
thread_9.join()