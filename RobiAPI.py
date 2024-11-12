from Connection import *


class RobiAPI:
    def __init__(
        self, hostname: str, port: int = 2000, protocolling: bool = False
    ) -> None:
        self.LINE_SEPARATOR = "\r\n"
        self.protocolling = protocolling
        self.sensorValues = [0] * 10
        self.connection = Connection(hostname, port)

    def connect(self) -> None:
        self.connection.connect()

    def disconnect(self) -> None:
        self.connection.disconnect()

    def protocol(self, order: str, answer: str) -> None:
        if self.protocolling:
            print(order + " " + answer)

    def setLeftDriveSpeed(self, speed: int) -> None:
        order = "setLeftDriveSpeed " + str(speed)
        self.connection.send(order + self.LINE_SEPARATOR)
        answer = self.connection.receive()
        self.protocol(order, answer)

    def setRightDriveSpeed(self, speed: int) -> None:
        order = "setRightDriveSpeed " + str(speed)
        self.connection.send(order + self.LINE_SEPARATOR)
        answer = self.connection.receive()
        self.protocol(order, answer)

    def drive(self, speed: int) -> None:
        order = "drive " + str(speed)
        self.connection.send(order + self.LINE_SEPARATOR)
        answer = self.connection.receive()
        self.protocol(order, answer)

    def turn(self, speed: int) -> None:
        order = "turn " + str(speed)
        self.connection.send(order + self.LINE_SEPARATOR)
        answer = self.connection.receive()
        self.protocol(order, answer)

    def stop(self) -> None:
        order = "stop"
        self.connection.send(order + self.LINE_SEPARATOR)
        answer = self.connection.receive()
        self.protocol(order, answer)

    def readSensor(self, sensorNumber: int) -> int:
        return self.sensorValues[sensorNumber]

    def getDistSensorValues(self) -> None:
        order = "getDistSensorValues"
        self.connection.send(order + self.LINE_SEPARATOR)
        answer = self.connection.receive()
        values = answer.split()
        for i in range(len(values)):  # bisher: range (16)
            self.sensorValues[i] = int(values[i])
        self.protocol(order, answer)

    def setPatternLED(self, r: int, c: int, state: bool) -> None:
        order = f"setPatternLED {r} {c} {state}"
        self.connection.send(order + self.LINE_SEPARATOR)
        answer = self.connection.receive()
        self.protocol(order, answer)

    def setPatternLEDColor(self, r: int, c: int, color: int) -> None:
        order = f"setPatternLED {r} {c} {color}"
        self.connection.send(order + self.LINE_SEPARATOR)
        answer = self.connection.receive()
        self.protocol(order, answer)
