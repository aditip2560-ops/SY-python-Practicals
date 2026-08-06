print("=====Billing Details=====")

rice_qty=float(input("Enter the qty of rice:"))
rice_price_per_kg=50
rice_total=rice_qty*rice_price_per_kg

suger_qty=float(input("Enter the qty of suger:"))
suger_price_per_kg=100
suger_total=suger_qty*suger_price_per_kg

oil_qty=float(input("Enter the qty of oil:"))
oil_price_per_kg=150
oil_total=oil_qty*oil_price_per_kg

print("=====Total Amount=====")

print("rice",rice_total)
print("suger",suger_total)
print("oil",oil_total)

total_bill=rice_total+suger_total+oil_total

print("total bill",total_bill)
Discount=0
if total_bill>=1000:
    Discount=total_bill*0.1
    print("Discount",Discount)
elif total_bill>=5000:
     Discount=total_bill*0.5
     print("Discount",Discount)
else :
     print("No Discount",Discount)

Final_bill=total_bill-Discount
print("final_bill",total_bill)