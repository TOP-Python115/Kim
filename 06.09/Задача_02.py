from datetime import datetime, timedelta

class period_of_the_day:
    def __init__(self, 
                 time: int = None, 
                 timezone: int = None, 
                 period: int = None, 
                 current_timezone: int = 3, 
                 delta: int = None):
        self.timezone = timezone
        self.time = time
        self.period = period
        self.current_timezone = 3
        self.delta = delta
    
    def calc_show_period(self):
        self.timezone = int(input('Enter timezone: '))
        if self.timezone > self.current_timezone:
            self.delta = timedelta(hours=self.timezone - self.current_timezone)
            time = datetime.now() + self.delta
        else:
            self.delta = timedelta(hours=self.current_timezone - self.timezone)
            time = datetime.now() - self.delta
        if time.hour < 6:
            period = 'night'
        elif time.hour >= 6 and time.hour < 12:
            period = 'morning'
        elif time.hour >= 12 and time.hour < 18:
            period = 'noon'
        elif time.hour > 18:
            period = 'evening'
        return period

res = period_of_the_day()
print(res.calc_show_period())
        
# Enter timezone: 9
# night
# >>>