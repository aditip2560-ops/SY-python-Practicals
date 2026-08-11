customer_name = input("Enter customer_name:")
product_name =input("Enter product_name:")
customer_feedback = input ("Enter feedback:")

customer_name = customer_name.strip().title()
product_name = product_name.strip().title()
customer_feedback = customer_feedback.strip().title()

print("======= customer_feedback=======")
print("customer_name:",  customer_name)
print("product_name:",product_name)
print("customer_feedback:", customer_feedback)

print("thank you for your feedback:")