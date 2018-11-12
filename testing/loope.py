def cel_to_fahr(celcius):
    fahrenheit = celcius * 9/5 +32
    return fahrenheit

temperatures = [10, -20, 100]

for c in temperatures:
    print(cel_to_fahr(c))
