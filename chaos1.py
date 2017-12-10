#this programma is to experiment with chaos with the following equation: f(x)=x*(1-x)*k
import time

def chaos1(x,k):
    y=x*(1-x)*k
    return y

def run():
    x=float(raw_input("Please enter a number for x: "))
    k=float(raw_input("Please enter a number for k: "))
    count=0

    try:
        while True:
        
            if (count==0):
                y=chaos1(x,k)
                count=1
                continue
            
            y=chaos1(y,k)

            count+=1

            print "The value of count %i" %(count)
            print "The value of y %f" %(y)

            if count>1000:
                break
            time.sleep(1)

    except KeyboardInterrupt:
           print "This programme has exited processing routine"

    print "Here are the final values %f  &  %i" %(y,count)

if(__name__=="__main__"):
    run()


        
                
