import sys,time

def delprint(text,delay_time): 
  for character in text:      
    sys.stdout.write(character) 
    sys.stdout.flush()
    time.sleep(delay_time)

delprint('fsdvibavdkbabasd', 0.04)