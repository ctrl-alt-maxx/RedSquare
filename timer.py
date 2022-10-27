import threading as th

def sctn() :
    print("Section for life")

S = th.Timer(5.0, sctn)
S.start()
print("Program finish")
S.cancel()