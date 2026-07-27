print("*****college admission  eligibility *****")
age =int(input ("Enter Your age :"))
marks =float(input ("Enter Your marks :"))

if age>=17 & age<=25:
    print("it is eligibal:")
    if marks>=60:
        print("it is eligibal:")
        if marks>=80:
              print("allow seat in AIML stream")
        elif marks>=60:
              print("allow seat in CSE stream")
        else:
              print("allow seat in general stream")
    else:
        print("it is not eligibal:")
else:
        print("it is not eligibal:")