import hashlib 
import time
from statistics import mean 

#Check SHA-256

ini_sha256 = "C0535E4B"
fin_sha256 = "1AD9E51A"
sha256 = hashlib.sha256(b"Hello world!").hexdigest()

print("--------------Validation of SHA-256-------------------------------")
print("SHA-256 4 first bytes", sha256[:8].upper())
print("Check that it matches with C0535E4B -->", ini_sha256.upper() == sha256[:8].upper())
print("---------------------------------------------")
print("SHA-256 4 first bytes", sha256[-8:].upper())
print("Check that it matches with 1AD9E51A -->", fin_sha256.upper() == sha256[-8:].upper())
print("---------------------------------------------")
print("\n\n\n")

#Check SHA-512

ini_sha512 = "F6CDE2A0"
fin_sha512 = "85FFB5B6"
sha512 = hashlib.sha512(b"Hello world!").hexdigest()

print("--------------Validation of SHA-512-------------------------------")
print("SHA-256 4 first bytes", sha256[:8].upper())
print("Check that it matches with F6CDE2A0 -->", ini_sha512.upper() == sha512[:8].upper())
print("---------------------------------------------")
print("SHA-256 4 first bytes", sha256[-8:].upper())
print("Check that it matches with 85FFB5B6 -->", fin_sha512.upper() == sha512[-8:].upper())
print("---------------------------------------------")
print("\n\n\n")


cache = bytes(256*1024*1024)
rates = []
times = []

for i in range(0,20):
  start = time.time() #measures seconds
  cache_sha256 = hashlib.sha256(cache).hexdigest()
  end =time.time()
  timming = end - start
  rate = 256/timming #MB/s
  times.append(timming)
  rates.append(rate)



avg_rate = round(mean(rates),11)
avg_time = round(mean(times),3)

print("--------------Performance Validation of SHA-256-------------------------------")
print('The average time it takes to process SHA-256 is {} ns. \nThis is an average rate of {} MB/s'.format(avg_time*1000000, avg_rate))
print("\n\n\n")

cache = bytes(256*1024*1024)
rates = []
times = []

for i in range(0,20):
  start = time.time() #measures seconds
  cache_sha256 = hashlib.sha512(cache).hexdigest()
  end =time.time()
  timming = end - start
  rate = 256/timming #MB/s
  times.append(timming)
  rates.append(rate)

print(times)
avg_rate = round(mean(rates),11)
avg_time = round(mean(times),3)

print("--------------Performance Validation of SHA-512-------------------------------")
print('The average time it takes to process SHA-512 is {} ns. \nThis is an average rate of {} MB/s'.format(avg_time*1000000, avg_rate))
print("\n\n\n")
