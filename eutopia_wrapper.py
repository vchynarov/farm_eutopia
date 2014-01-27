from eutopia import *

if __name__=='__main__':

    interventions = []
    eutopia_sim = Eutopia() # renamed to avoid naming conlicts (ie eutopia.py)
    
    interventions.append(intervention.PriceIntervention(5, 'duramSeed', 10))

    interventions.append(intervention.PriceIntervention(7, 'duramSeedOrganic', 0.001))

    magic_activity = {
        'equipment': ['tractor', 'wheelbarrow'],
        'products': {
            'duramSeed': -5,
            'nitrogen': -10,
            'carbon': 20,
            'soil': -5,
            'labour': -2000,
            'certification': 0,
            'duram': 1000000,
            'dolphin': -87,
            }
        }
    interventions.append(intervention.NewActivityIntervention(7, 'magic', magic_activity))    
    
    
    time = 0
    def step():
        global time
        for intervention in interventions:
            if time >= intervention.time:
                intervention.apply(eutopia_sim, time)
        time += 1
    
        eutopia_sim.step()
    
    
    activities = []
    for i in range(10):
        step()
        activities.append(eutopia_sim.get_activity_count())
        
    print activities    
    
