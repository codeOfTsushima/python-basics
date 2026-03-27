def ms( * top, **si):
    for topp in top:
        print(f"- {topp}")
        
    for key, value in si.items():
        print(f"{key},{value}")
        
ms("bacon", "lettuce", "tomato", bread="wheat", sauce="ranch", toasted=True)