import time as t

my_time = t.localtime()
print(my_time)
current_transaction = ("Transaction has been Completed at "+ str(my_time.tm_hour) +"h"+ str(my_time.tm_min)+"m"+str(my_time.tm_sec)+"s")
print(current_transaction)

time_now = t.time()
print(time_now)

delivery_time = time_now + (86400 * 7)

print(t.localtime(delivery_time))
