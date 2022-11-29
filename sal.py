def salary(company):

	print(f"\nFor {company}:")

	if company == "APTIV":
		pretaxnet = 1650995
		taxable1 = 1386595
		basic = 65967
		foodcost = 3000
		bonus = 0

	elif company == "MERCEDES":
		pretaxnet = 1443074
		taxable1 = 1178674
		basic = 47532
		foodcost = 0
		bonus = 142596

	rent = [i* 1000 for i in range(9, 20)]

	hra = [12*min(0.4*basic, (r - 0.1*basic)) for r in rent]

	taxable2 = [(taxable1  - h) for h in hra]

	finaltax = [1.04*(112500 + 0.3*(t2 - 1000000)) if t2>1000000 else (12500 + 0.2*(t2 - 500000)) for t2 in taxable2]

	netpay_rentout = [(((pretaxnet - f)/12) - rent[i]) for i, f in enumerate(finaltax)]

	for i, r in enumerate(rent):
		print(f"For rent of {r}, net - rent - food + bonus : {int(netpay_rentout[i]) - foodcost }")

if __name__ == '__main__':
	
	salary("APTIV")
	salary("MERCEDES")