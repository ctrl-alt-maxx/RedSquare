import c31Geometry2 as c31
import play as p

class Check:
    
    def check(num):
        if num < 150:
            eventCheck.eventPlay()
        elif num >= 150:
            eventCheck.eventStop()
            
class eventCheck:
    
    def eventPlay(event):
        event.stop()
    
def eventStop(event):
        event.start()