import sys
try: 
    list = [3,7, 9, 4, 6] 
    print (list[6])
except IndexError as e: 
    print (e)
sys.exit()

