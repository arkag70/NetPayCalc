from company import Company

if __name__ == '__main__':
	
	aptiv = Company("Aptiv", 1650995, 65967, 3000, 0)
	mercedes = Company("Mercedes", 1443074, 47532, 0, 142596)
	gehealthcare = Company("GE Healthcare", 1650000, 63333, 3000, 190000)

	companies = [aptiv, mercedes, gehealthcare]

	for company in companies:
		company.salary()