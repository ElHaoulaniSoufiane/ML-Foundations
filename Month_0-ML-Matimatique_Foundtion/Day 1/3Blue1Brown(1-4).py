class Vector:
    def __init__(self, vector:list):
        self.vector = vector

    def add(self, new_vector):
        if len(self.vector) != len(new_vector):
            raise ValueError("The Lenght Must Be The Same")
        return Vector([self.vector[i] + new_vector[i] for i in range(len(self.vector))])
    
    def sub(self, new_vector):
        if len(self.vector) != len(new_vector):
            raise ValueError("The Lenght Must Be The Same")
        return Vector([self.vector[i] - new_vector[i] for i in range(len(self.vector))])

    def scale(self, scaller):
        if type(scaller) not in (float,int):
            raise TypeError("The Type Must Be Type Int or Float")
        return Vector([i * scaller for i in self.vector])

    def dot(self, new_vector):
        if len(self.vector) != len(new_vector):
            raise ValueError("The Lenght Must Be The Same")
        prep = ([self.vector[i] * new_vector[i] for i in range(len(self.vector))])
        return sum(prep)

    def magnitude(self):
        return sum(i**2 for i in self.vector) ** 0.5

    def normalized(self):
        return Vector([i/self.magnitude() for i in self.vector])