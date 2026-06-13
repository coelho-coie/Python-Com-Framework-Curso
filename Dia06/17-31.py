class Drone:
    def __init__(self):
        self.altitude = 10
        self.bateria = 100
        self.gps = [0, 0]

    def mover(self, x, y):
        if self.bateria >= 5:
            self.gps = [x, y]
            self.bateria -= 5
        else:
            self.altitude = 0
            print("Bateria crítica! Pousando...")

d = Drone()
d.mover(10, 20)
print(f"Posição: {d.gps}, Bateria: {d.bateria}%")