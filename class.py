class Speed:
    def __init__(self, distance, time):
        self.distance = distance
        self.time = time
    def calculate_velocity(self):
        velocity = self.distance / self.time
        return velocity

distance = float(input("Введите расстояние (в метрах): "))
time = float(input("Введите время (в секундах): "))
speed = Speed(distance, time)
print("Скорость равна", speed.calculate_velocity(), "м/с")
