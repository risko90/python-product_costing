#Let the user know that this costing has started and after hitting ENTER
#he or she can either select current data or modify variables.

print ('Costing calculator is now running.')
print ('After pressing ENTER you can select current data as base or adjust these yourself.')
print (' ')
input ('Press ENTER to continue: ') 

#Describe user the product and production space.
print ('We need to calculate table flag selling price for 900PCs per month.')
print ('Flag has 4 different components in bill of material.')
print ('Office and production is in the same small room.')
print ('Office and production worker work full-time.')
print (' ')
print ('Here are current cost levels and figures')
#Set up all needed variables with data and print them to user.
operatorcost = 1000
officesalary = 1500
averagehours = 156
scraprate = 1/100
packagingcost = 0.01 #packaging cost per PC
profitpercent = 1/10
roomrent = 500 #roomrent including electricity, internet etc...
machinery = 100
print ('Operator cost per month =', operatorcost,'EUR')
print ('Average monthly working hours =', averagehours)

#After printing ask user if they want to change them and ask to change one by one, typing y = yes and n = no



#Here you need to input common costing parameters. How much is work time per PC etc...
assembling = 1 #One minute per PC
packing = 0.01 #


compflagpole = 0.05 #price per PC
compflag = 0.30 #price per meter length
compyarn = 0.03 #price per meter length
compbase = 0.04 #price per PC
print (' ')
print (' ')
print ('Bill of Material is as follows:')
print ('One flag pole, cost per PC =', compflagpole,'EUR')
print ('0.10m long flag, cost per meter length =', compflag,'EUR')
print ('0.50m yarn, cost per meter length =', compyarn,'EUR')
print ('One base for flag standing, cost per PC =', compbase,'EUR')
print (' ')

#Set variables for flag and yarn - quanitity needed per one finish product.
flagquant = 0.1
yarnquant = 0.5
BOMcost = compflagpole + (compflag * flagquant) + (compyarn * yarnquant) + compbase

#print random formulas as test
print ('BOM cost per PC =', BOMcost,'EUR')

