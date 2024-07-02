import sys,time

def delprint(text,delay_time): 
  for character in text:      
    sys.stdout.write(character) 
    sys.stdout.flush()
    time.sleep(delay_time)

delprint('Eu sou um texto de teste, não se preocupe comigo.\n', 0.04)