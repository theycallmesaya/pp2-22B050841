import re
def f(mObject):
    return mObject.group("g1")+ "_" + mObject.group("g2").lower()
text = "mySuperVar" #camel case