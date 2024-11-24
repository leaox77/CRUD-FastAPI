# map (Elevar al cuadrado)
data = [1,2,3,4,5,6]

## Using comprehension 
new_data = [x**2 for x in data] 

## Using map
new_data = map(lambda x: x**2, data)

## Results
print(f"Map results: {new_data}")
print(f"Map results (list): {list(new_data)}")

## Iterating object
for x in new_data:
    print(x, end=",")
print()

# filter (Obtener los pares de una lista)
data = [1,2,3,4,5,6]

## Using comprehension
new_data = [x for x in data if x % 2 == 0]

## Using filter
new_data = filter(lambda x: x%2 == 0, data)

## Results
print(f"Filter results: {new_data}")

