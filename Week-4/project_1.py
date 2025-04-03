Girls = [('Evelyn',17,5.5,80), ('Jessica',16,6.0,85), ('Somto',17,5.4,70), ('Edith',18,5.9,60), ('Liza',16,5.6,76), ('Madonna',18,5.5,66,), ('Waje',17,6.1,87), ('Tola',20,6.0,95), ('Aisha',19,5.7,50), ('Latifa',17,5.5,49)]
Boys = [('Chinedu',19,5.7,74), ('Liam',16,5.9,67), ('Wale',18,5.6,73), ('Gbenga',17,6.1,68), ('Abiola',20,5.9,66), ('Kola',19,5.5,79), ('Kunle',16,6.1,97), ('George',18,5.4,90), ('Thomas',17,5.8,54), ('Wesley',19,5.7,60)]
print("_______________________________")
print("Name     | Age | Height | Score")
print("_______________________________")
for name,age,height,score in Girls:
    output = f"{name:<9}|{age:<5}|{height:<8}|{score:<6}"
    print(output)
for name,age,height,score in Boys:
    output = f"{name:<9}|{age:<5}|{height:<8}|{score:<6}"
    print(output)