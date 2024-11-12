from datetime import datetime, timedelta


class HourGlass:
    def __init__(self) -> None:
        self.startTime = datetime.now()

    def start(self, durationInMilliSeconds: int) -> None:
        self.startTime = datetime.now()
        self.duration = durationInMilliSeconds

    def timeOut(self) -> bool:
        return datetime.now() >= (self.startTime + timedelta(milliseconds=self.duration))
