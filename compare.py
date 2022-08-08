import sys
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
                            # if all values are equal, print line
                            print("Found perfect match: ")
                            print(index, i)
                            #print(row)
                            # save i and index into matches list
                            matches.append([i, index])
                        else:
                            # if Tax_Value is not equal, print line
                            print("Found match with different Tax_Value: ")
                    # if Quantity is not equal to systemQuantity, break out of loop
                    else:
                        print("Found mismatch in Quantity: ")
                        #print indexes
                        print(index, i)
                # if Tax_Code is not equal to systemTax_Code, break out of loop
                else:
                    print("Found mismatch in Tax_Code: ")
                    # print systemRow and ficheRow
                    print(index, i)
            # if DeclaredValue is not equal to systemDeclaredValue, break out of loop
            else:
                print("Found mismatch in DeclaredValue: ")
                print(index, i)
        

print(matches)
# remove matches from ficheDF and systemDF
for i in matches:
    ficheDF = ficheDF.drop(i[0])
    systemDF = systemDF.drop(i[0])

print(ficheDF)
print(systemDF)


