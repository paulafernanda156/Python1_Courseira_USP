def F (P, x) :
    result = 0
    for exponent, coeficient in enumerate (P) :
        result += coeficient * x ** exponent
        return result

     def F(P, x) :
         return sum(c * x ** e for (e, c) in enumerate(P)) 

class Poli:
    def __init__(self, coeficients) :
        self.coeficients = coeficients
        @property
        def degree(self) :
            return len(coeficients) - 1
        def __call__(self, x):
            return sum(c * x ** e for (e,c ) in enumerate(self.coeficients))    
        def __repr__(self):
            return f"P ({})".format(" + ".join(f"{c} * x ** {e}" for e, c in enumerate(self.coeficients))