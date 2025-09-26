from datetime import datetime, timedelta

class CalendarScheduler:
    def schedule(self, optimal_times):
        calendar = {}
        for i in range(7):
            date = (datetime.now() + timedelta(days=i)).strftime("%Y-%m-%d")
            calendar[date] = {
                "times": optimal_times,
                "status": "pending"
            }
        return calendar
