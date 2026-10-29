time = int(input("Enter homework time in minutes: "))

if time > 60:
    plan = "start homework now"
    print("That is a long homework session.")
else:
    plan = "finish homework quickly"
    print("That is a short session.")

free_time = input("Is there free time after homework? (yes/no): ")
if free_time == "yes":
    print("Pick a hobby!")
else:
    print("")

print("==== Daily Plan ====")
print("Homework Minutes:", time)
print("Plan:", plan)
print("Free time:", free_time)
print("=========================================")