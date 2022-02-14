import imp
from tqdm import tqdm, trange
from colorama import init, Fore, Back, Style
import time

print(Fore.GREEN)
for i in tqdm([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]):
    time.sleep(0.2)