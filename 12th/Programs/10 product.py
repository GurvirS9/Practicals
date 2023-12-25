import csv
fields = ['Product ID', 'Product Name', 'Product Price']
file = 'product.csv'

def addrec():
    with open(file, 'w', newline='') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(fields)
        ch = 'y'
        while ch == 'y':
            prodid = eval(input("Enter Product ID: "))
            prodname = input("Enter Product Name: ")
            prodprice = eval(input("Enter Product Price: "))
            rec = [prodid, prodname, prodprice]
            csvwriter.writerow(rec)
            ch = input("Want to enter more products? (y/n): ")
        print("CSV file created successfully")
    f.close()

def price100():
    with open(file, 'r') as f:
        data = csv.reader(f)
        next(data)
        for row in data:
            if int(row[2]) > 100:
                print(row)
            else:
                continue
    f.close()

ch = 'y'
while ch == 'y':
    print("-----------------------")
    print("          Menu            ")
    print("-----------------------")
    print("1. Create File and Add Records")
    print("2. Display records with price more than 100")
    c = eval(input("Enter choice: "))
    if c == 1:
        addrec()
    elif c == 2:
        price100()
    else:
        print('Invalid choice')
    ch = input('Continue? (y/n): ')
