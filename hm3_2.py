import time
import multiprocessing as mp
from concurrent.futures import ProcessPoolExecutor

def factorize(*numbers):
    
    res_numbers = []
    
    for number in numbers:
        res_number = []
        for i in range(1, number + 1):
            if number % i == 0:
                res_number.append(i)
        res_numbers.append(res_number)
    return res_numbers



if __name__ == '__main__':
    print("Start without multiprocessing")
    start = time.time()
    a, b, c, d = factorize(128, 255, 99999, 10651060)
    print("Time without multiprocessing: ", time.time() - start)
    print("Start with multiprocessing")
    start = time.time()
    with ProcessPoolExecutor(mp.cpu_count()) as executor:
        a, b, c, d = executor.map(factorize, (128, 255, 99999, 10651060))
    print("Time with multiprocessing: ", time.time() - start)
    print(f"128: {a}\n255: {b}\n99999: {c}\n10651060: {d}")
    