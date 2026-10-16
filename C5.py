
# C5: Star-Delta (Y-delta) Transformation

def star_delta(Ra, Rb, Rc):
    numerator = Ra * Rb + Rb * Rc + Rc * Ra
 
    Rab = numerator / Rc
    Rbc = numerator / Ra
    Rca = numerator / Rb
 
    return round(Rab, 2), round(Rbc, 2), round(Rca, 2)
 
 
print("star_to_delta(10, 20, 30) ->", star_delta(10, 20, 30))
