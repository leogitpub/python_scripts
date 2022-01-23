def print_models(unprinted, printed):
    while unprinted:
        current_model = unprinted.pop()
        print('printing the current model' + current_model)
        printed.append(current_model)

# we are going to print some empty lists

unprinted = ['ear', 'mobile', 'chrager']
printed = []
print_models(unprinted, printed)
if unprinted != "":
  for printes in unprinted:
     print("\nUnprinted is empty:" + printes)
if printed != "":
    for printe in printed:
        print("printed" + printe)
print(":::::::::::::::::::::::::::::::::::::::")

unprinted = ['amingo', 'mobile-prohones', 'chrager-socket']
printed = []
print_models(unprinted[:], printed)

if unprinted != "":
    for printes in unprinted:
        print("\nUnprinted is not empty:" + printes)

if printed != "":
    for printees in printed:
        print("\nprinted:" + printees)

print("::::::::::::::::::::::::::::::::::::::::")

original = ['ear', 'mobile', 'chrager']
printed = []
print_models(original[:], printed)

if original != "":
    for printes in original:
        print("\nOriginal:" + printes)

if printed != "":
    for printees in printed:
        print("\nprinted:" + printees)

