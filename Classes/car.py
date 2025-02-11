class Car:
    def start(self):
        print(f"{self.model} is started")  
    def stop(self):
        print(f"{self.model} is stoped")

Tasla = Car()
Carola = Car()
Honda = Car()

Tasla.model = "Model S"
Tasla.color = "Black"
Tasla.year = "2024"

Carola.model = "Carola GLI"
Carola.color = "White"
Carola.year = "2020"



Tasla.start()
Carola.start()

Tasla.stop()

