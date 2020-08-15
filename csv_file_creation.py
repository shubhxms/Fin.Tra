import csv
print("hello")

def create_file():
    #creating outgo csv file
    try:
        outgo = open("outgo.csv", 'r')
    except FileNotFoundError:
        outgo = open("outgo.csv",'w')
        writer = csv.writer(outgo, delimiter=',')
        outgo_header = ['MONTHS','purchase','electricity','telecom','rent','interest','depri','salary','wages','maintenance','tax','travelling','advt','capital-expenses','inventory-costs','insurance','misc']
        writer.writerow(outgo_header)
        #months = ["Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec", "Jan","Feb","Mar"]months = ["April","May","June","July","August","September","October","November","December", "January","February","March"]
        months = ["Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec", "Jan","Feb","Mar"]
        for month in months:
            record = [month]
            writer.writerow(record)
        outgo.close()

    #creating income csv file
    try:
        income = open("income.csv", 'r')
    except FileNotFoundError:
        income = open("income.csv", 'w')
        writer = csv.writer(income, delimiter=',')
        income_header = ['MONTHS','sales','interest','rent','bad-debts','misc']
        writer.writerow(income_header)
        months = ["Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec", "Jan","Feb","Mar"]
        for month in months:
            record = [month]
            writer.writerow(record)
        income.close()