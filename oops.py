#1
##class phone:
##    pass
##ph1 = phone()
##ph2 = phone()
##
##ph1.color="black"
##ph1.company="samsang"
##ph1.ram= 4
##
##ph2.color="white"
##ph2.company="iphone"
##ph2.ram= 2
##
##print(ph1.color)
##print(ph2.ram)


#BIF:
class phone:
    def __init__(self,color,company,ram):
        self.color = color
        self.company = company
        self.ram = ram
ph1 = phone("black","samsung",4)
ph2 = phone("white","iphone",2)
print(ph1.color)
print(ph2.company)


###2
##class nuclear:
##    pass
##n1 = nuclear()
##n2 = nuclear()
##
##n1.name = "Atomic bomb"
##n1.range = "8.6 km"
##n1.weight = "10 mt"
##
##
##n2.name = "Dirty bomb"
##n2.range = "4.8 km"
##n2.weight = "50 mt"
##
##print(n1.range)
##print(n2.name)

#3
##class Space:
##    pass
##s1 = Space()
##s2 = Space()
##
##s1.GalaxyName = "Milky Way"
##s1.planets = "Earth"
##s1.LivingPlanets = "1 was identified"
##
##s2.GalaxyName = "Andromeda"
##s2.planets = "PA-99-N2"
##s2.LivingPlanets = "Unidentified"
##
##print(s1.GalaxyName,",",s1.planets,",",s1.LivingPlanets )
##print(s2.GalaxyName,",",s2.planets,",",s2.LivingPlanets)
##
