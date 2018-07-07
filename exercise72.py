import glob2
from datetime import datetime

filenames = glob2.glob('temp/*.txt')
#print(filenames)

with open(datetime.now().strftime("%Y-%m-%d, %H.%M.%S")+".txt", 'w') as file:
    for filename in filenames:
        with open(filename, 'r') as f:
            file.write(f.read() + '\n')