import collections
import time
from threading import Timer

class LRU:
    def __init__(self, size,clear_time):
        self.size = size
        self.cache = collections.OrderedDict()  #to generate key and value for cache items
        self.start_time=time.time()
        self.clear_time=clear_time
        
    #retrieve previous set data    
    def __getitem__(self, k):
            value = self.cache.pop(k)
            self.cache[k] = value
            return value
        
    # set the cache value and key    
    def __setitem__(self, k, value):
            try:
               #pop the old key 
               self.cache.pop(k)
            except KeyError:
                if len(self.cache) >= self.size:
                    #remove the least used cache from the rare of the queue
                    #if exceed the assigned size
                    self.cache.popitem(last=False)                 
                       
            current_time = time.time()
            
            if (round(current_time-self.start_time)) == self.clear_time:
                self.timer()
                self.cache[k] = value
            else:
                self.cache[k] = value
                
            
    #clear cache        
    def clearCache(self):
       self.cache.clear()
       
    def timer(self):
         Timer(self.clear_time,self.clearCache,()).start()
         
