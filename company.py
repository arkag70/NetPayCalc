medical80D = 13000

class Company:

    def __init__(self, name, pretaxnet, basic, food, bonus):

        self.name = name
        self.pretaxnet = pretaxnet
        self.basic = basic
        self.food = food
        self.bonus = bonus

    def salary(self):

        print(f"\nFor {self.name}:")
        
        taxable1 = self.pretaxnet - 252400 - medical80D #+ self.bonus

        rent = [i* 1000 for i in range(9, 20)]

        hra = [12*min(0.4*self.basic, (r - 0.1*self.basic)) for r in rent]

        taxable2 = [(taxable1 - h) for h in hra]

        finaltax = [1.04*(112500 + 0.3*(t2 - 1000000)) if t2>1000000 else (12500 + 0.2*(t2 - 500000)) for t2 in taxable2]

        netpayout = [(((self.pretaxnet - f)/12)) for i, f in enumerate(finaltax)]

        for i, r in enumerate(rent):
            print(f"For rent of {r}, net : {int(netpayout[i])}")
        print(f"With an annual bonus of : {self.bonus}")

    