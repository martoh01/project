print("Re-Adjusting the values to 123456...")

for i in ["easy", "medium", "hard"]:
    with open(f"Scores/{i}","w") as s1:
	    s1.write("987654")

print("Re_Adjustiment is Successful")

