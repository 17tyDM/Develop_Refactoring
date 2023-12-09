import random
import timeit

def generate_million():
    global million 
    #million = set(random.choices(range(0, 10000000001), k=1000000))
    million = set([random.randint(0, 10000000000) for _ in range(1000000)])

def generate_hundred():
    global hundred
    #hundred = set(random.choices(range(0, 10000000001), k=100))
    hundred = set([random.randint(0, 10000000000) for _ in range(100)])

def comparison(million_set, hundred_set):
    for i in hundred_set:
        if i in million_set:
            print(i)
    #print(million_set & hundred_set)

if __name__ == "__main__":
    time1 = timeit.timeit(lambda: generate_million(), number=1)
    print(len(million))
    time2 = timeit.timeit(lambda: generate_hundred(), number=1)
    print(len(hundred))
    time3 = timeit.timeit(lambda: comparison(million, hundred), number=1)
    print(f"[Million生成]実行時間：{time1:.6f}")
    print(f"[Hundred生成]実行時間：{time2:.6f}")
    print(f"[比較]実行時間：{time3:.6f}")
    print(f"[合計]実行時間：{time1+time2+time3:.6f}")
