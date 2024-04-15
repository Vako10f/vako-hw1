triangle=input("შენი სამკუთხედი როგორი სამკუთხედია?ბლაგვკუთხა,მახვილკუთხა თუ მართკუთხა")
if triangle == "ბლაგვკუთხა":
    ftriagle = input("შემოიტანე პირველი კუთხის გრადუსი")
    Mtriagle = input("შემოიტანე მეორე კუთხის გრადუსი")
    print(180-ftriagle-Mtriagle)
elif triangle == "მახვილკუთხა":
    ktriagle = input("შემოიტანე პირველი კუთხის გრადუსი")
    vtriagle = input("შემოიტანე მეორე კუთხის გრადუსი")
    print(180-ktriagle-vtriagle)
elif triangle == "მართკუთხა":
     btriagle = input("შემოიტანე პირველი კუთხის გრადუსი")
     print(180-90-btriagle)
else :
    print("დაწერე ქართული შრიფტით")