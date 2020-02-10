from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def start(self):
        """주행 시작"""
        pass

    def stop(self):
        """주행 정지"""
        self.speed = 0

    @property
    @abstractmethod
    def speed(self):
        pass


print(Vehicle.mro())
print(dir(Vehicle))