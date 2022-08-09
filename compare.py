import pandas as pd

ficheDF = pd.read_excel("output.xlsx")
systemDF = pd.read_excel("system.xlsx")

# set option to show all rows
pd.set_option('display.max_rows', None)

# set option to show all columns
pd.set_option('display.max_columns', None)

# display dataframe
print(ficheDF)
print(systemDF)


# index 0: SH_Codes
# index 1: DeclaredValues
# index 2: Tax_Codes
# index 3: Quantities
# index 4: Tax_Values

matches = []

# loop through each line in ficheDF and check if line is in systemDF
for index, row in ficheDF.iterrows():
    # check if SH_Code is in systemDF
    if row[0] in systemDF['SH_Codes']:
        # get list of indexes of row in systemDF
        indexList = systemDF[systemDF['SH_Codes'] == row[0]].index
        # loop through each index in indexList
        for i in indexList:
            # check if DeclaredValue is equal to systemDeclaredValue
            if row[1] == systemDF['DeclaredValues'][i]:
                # check if Tax_Code is equal to systemTax_Code
                if row[2] == systemDF['Tax_Codes'][i]:
                    # check if Quantity is equal to systemQuantity
                    if row[3] == systemDF['Quantities'][i]:
                        # check if Tax_Value is equal to systemTax_Value
                        if row[4] == systemDF['Tax_Values'][i]:
                            #print("Found perfect match: ")
                            #print(index, i)
                            # save i and index into matches list
                            matches.append([i, index])
                            break

print(matches)
# remove matches from ficheDF and systemDF
for i in matches:
    ficheDF = ficheDF.drop(i[0])
    systemDF = systemDF.drop(i[0])

print(ficheDF)
print(systemDF)

corrected = []
# correct errors in DeclaredValues and Tax_Values and Quantities
for index, row in ficheDF.iterrows():
    # check if SH_Code is in systemDF
    if row[0] in systemDF['SH_Codes']:
        # get list of indexes of row in systemDF
        indexList = systemDF[systemDF['SH_Codes'] == row[0]].index
        # loop through each index in indexList
        for i in indexList:
            # check if Tax_Code is equal to systemTax_Code
            if row[2] == systemDF['Tax_Codes'][i]:
                # replace systemDeclaredValue with ficheDeclaredValue
                systemDF['DeclaredValues'][i] = row[1]
                # replace systemTax_Value with ficheTax_Value
                systemDF['Tax_Values'][i] = row[4]
                # replace systemQuantity with ficheQuantity
                systemDF['Quantities'][i] = row[3]
                # save i and index into corrected list
                corrected.append([i, index])
                break

# remove corrected from ficheDF and systemDF
for i in corrected:
    ficheDF = ficheDF.drop(i[0])
    systemDF = systemDF.drop(i[0])

# the algorithm:

# count number of lines left, each line is a bit for a binary number, loop through each number in binary and check if sumQuantity is equal to systemQuantity
# if sumQuantity is equal to systemQuantity, check if sumDeclaredValue is close enough to systemDeclaredValue
# then get current binary number and add it to matches list
# if sumQuantity is not equal to systemQuantity, go to next binary

# count number of lines left
linesLeft = ficheDF.shape[0]
print(linesLeft)

# loop through each lineLeft
for i in range(linesLeft):
    # loop through each binary number
    for j in range(2**linesLeft):
        # get binary representation of j
        binary = bin(j)[2:]
        # get sumQuantity
        sumQuantity = 0
        for k in range(linesLeft):
            if binary[k] == '1':
                # add quantity to sumQuantity
                sumQuantity += ficheDF['Quantities'][k]
        # check if sumQuantity is equal to systemQuantity
        if sumQuantity == systemDF['Quantities'][i]:
            # get sumDeclaredValue
            sumDeclaredValue = 0
            for k in range(linesLeft):
                if binary[k] == '1':
                    # add quantity to sumDeclaredValue
                    sumDeclaredValue += ficheDF['DeclaredValues'][k]
            # check if sumDeclaredValue is close enough to systemDeclaredValue
            if abs(sumDeclaredValue - systemDF['DeclaredValues'][i]) < 0.01:
                # get current binary number
                currentBinary = j
                # add currentBinary to matches list
                matches.append([currentBinary, i])
                break