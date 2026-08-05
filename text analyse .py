text = input("Enter a paragraph")

characters = len(text)

spaces = text.count(" ")

words = len(text.split())

vowels = "aeiouAEIOU"
vowels_count = 0
for i in text :
    if i in vowels:
        vowels_count += 1

print("\n======== text analysis =======")
print(" Total characters ", characters)
print(" Total words  ", words )
print(" Total spaces ", spaces)
print(" Total vowels ", vowels_count )

if len(text)>0:
     print("\n first character (indexing)",text[:10])
     print(" last character (indexing) ",text[-10:])
print("\n firstt 10 character (slicing):",text[:10])
print("\n last 10 character (slicing):",text[-10:])