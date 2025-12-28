

def Single(Income): #Single
    if Income < 0:
        Tax = 0
    elif Income <= 8350:
        Tax = Income * 0.10
    elif Income <= 33950:
        Tax = (8350 * 0.10) + ((Income - 8350) * 0.15)
    elif Income <= 82250:
        Tax = (8350 * 0.10) + (25600 * 0.15) + ((Income - 33950) * 0.25)
    elif Income <= 171550:
        Tax = (8350 * 0.10) + (25600 * 0.15) + (48300 * 0.25) + ((Income - 82250) * 0.28)
    elif Income <= 372950:
        Tax = (8350 * 0.10) + (25600 * 0.15) + (48300 * 0.25) + (89300 * 0.28) + ((Income - 171550) * 0.33)
    elif Income > 372950:
        Tax = (8350 * 0.10) + (25600 * 0.15) + (48300 * 0.25) + (89300 * 0.28) + (201400 * 0.33) \
            + ((Income - 372950) * 0.35)
    return Tax
def MarriedFJoQWidow(Income): #Married Filing Jointly or Qualified Widow(er)
    if Income < 0:
        Tax = 0
    elif Income <= 16700:
        Tax = Income * 0.10
    elif Income <= 67900:
        Tax = (16700 * 0.10) + ((Income - 16700) * 0.15)
    elif Income <= 137050:
        Tax = (16700 * 0.10) + (51200 * 0.15) + ((Income - 67900) * 0.25)
    elif Income <= 208850:
        Tax = (16700 * 0.10) + (51200 * 0.15) + (69150 * 0.25) + ((Income - 137050) * 0.28)
    elif Income <= 372950:
        Tax = (16700 * 0.10) + (51200 * 0.15) + (69150 * 0.25) + (71800 * 0.28) + ((Income - 208850) * 0.33)
    elif Income > 372950:
        Tax = (16700 * 0.10) + (51200 * 0.15) + (69150 * 0.25) + (71800 * 0.28) + (164100 * 0.33) \
            + ((Income - 372950) * 0.35)
    return Tax
def MarriedFS(Income): #Married Filing Seperately
    if Income < 0:
        Tax = 0
    elif Income <= 8350:
        Tax = Income * 0.10
    elif Income <= 33950:
        Tax = (8350 * 0.10) + ((Income - 8350)* 0.15)
    elif Income <= 68525:
        Tax = (8350 * 0.10) + (25600 * 0.15) + ((Income - 33950) * 0.25)
    elif Income <= 104425:
        Tax = (8350 * 0.10) + (25600 * 0.15) + (34575 * 0.25) + ((Income - 68525) * 0.28)
    elif Income <= 186475:
        Tax = (8350 * 0.10) + (25600 * 0.15) + (34575 * 0.25) + (35900 * 0.28) + ((Income - 104425) * 0.33)
    elif Income > 186475:
        Tax = (8350 * 0.10) + (25600 * 0.15) + (34575 * 0.25) + (35900 * 0.28) + (82050 * 0.33) \
            + ((Income - 186475) * 0.35)
    return Tax
def HeadoHouse(Income): #Head of Household
    if Income < 0:
        Tax = 0
    elif Income <= 11950:
        Tax = Income * 0.10
    elif Income <= 45500:
        Tax = (11950 * 0.10) + ((Income - 11950) * 0.15)
    elif Income <= 117450:
        Tax = (11950 * 0.10) + (33550 * 0.15) + ((Income - 45500) * 0.25)
    elif Income <= 190200:
        Tax = (11950 * 0.10) + (33550 * 0.15) + (71950 * 0.25) + ((Income - 117450) * 0.28)
    elif Income <= 372950:
        Tax = (11950 * 0.10) + (33550 * 0.15) + (71950 * 0.25) + (72750 * 0.28) + ((Income - 190200) * 0.33)
    elif Income > 372950:
        Tax = (11950 * 0.10) + (33550 * 0.15) + (71950 * 0.25) + (72750 * 0.28) + (182750 * 0.33) \
            + ((Income - 372950) * 0.35)
    return Tax
def PersonalIncomeTax(): #Instructions for user
    print("FILING STATUSES\n" \
    "0 - Single\n" \
    "1 - Married Filing Jointly or Qualified Widow(er)\n" \
    "2 - Married Filing Seperately\n" \
    "3 - Head of Household\n")
    print("Enter the number corresponding to your filing status.\n")
#Beginning of Program
PersonalIncomeTax()
while True:
    filing_status = int(input("filing_status: "))
    income = int(input("Your Income: "))
    income = float(income)
    if filing_status not in [0,1,2,3]:      
          print("Invalid filing status! Please re-enter.")
    elif filing_status == 0:
        print(f"Your Tax Rate = ${Single(income):.2f}")
        break
    elif filing_status == 1:
        print(f"Your Tax Rate = ${MarriedFJoQWidow(income):.2f}")
        break
    elif filing_status == 2:
        print(f"Your Tax Rate = ${MarriedFS(income):.2f}")
        break
    elif filing_status == 3:
        print(f"Your Tax Rate = ${HeadoHouse(income):.2f}")
        break