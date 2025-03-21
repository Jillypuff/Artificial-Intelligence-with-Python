from logic import *

rain = Symbol("rain") # It is raining
hagrid = Symbol("hagrid") # Harry visited Hagrid
dumbledore = Symbol("dumbledore") # Harry visited Dumbledore

knowledge = And(
    Implication(
    Not(rain), hagrid),
    Or(hagrid, dumbledore),
    Not(And(hagrid, dumbledore)),
    dumbledore
) # If it is not raining, then Harry visited Hagrid

print(model_check(knowledge, dumbledore))
