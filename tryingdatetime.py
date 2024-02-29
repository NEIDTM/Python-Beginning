import datetime
from datetime import datetime

def new_year():
    timenow = datetime.today()
    print(f"Today is: {timenow}")
    newyear = datetime(timenow.year + 1, 1, 1, 0, 0, 0)
    timeleft = newyear - timenow
    print(f"{timeleft.days} days left until the New year!")

new_year()
