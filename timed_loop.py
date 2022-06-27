import time

iterator = 0

start_time = time.time()

while iterator < 10000:
    iterator += 1
    print(iterator)

end_time = time.time()
print("\nElapsed time: %.6f" %(end_time - start_time))