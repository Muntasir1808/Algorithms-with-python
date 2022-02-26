has_high_income = True
has_good_credit = True
not_criminal_record = True
print("For And logic")
if has_high_income and has_good_credit:
    print("Eligible for loan")
else:
    print("Not eligible")
print("---And logic finishes---")

if has_good_credit and not_criminal_record:
    print("Yes,he's eligible for loan")