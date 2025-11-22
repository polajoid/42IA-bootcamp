from tqdm import tqdm
from time import sleep


def ft_progress(lst):
    for i in tqdm(lst, desc="ETA: ", total=len(lst), ascii=" >="):
        yield i


listy = range(3333)
ret = 0
for elem in ft_progress(listy):
    ret += elem
    sleep(0.005)
print()
print(ret)
