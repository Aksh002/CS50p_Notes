input=input("Input: ")
output=""
for z in input:
    if z  not in ('a','e','i','o','u'):
        output=output + z
    else:
        continue
print("Output: ",output)

