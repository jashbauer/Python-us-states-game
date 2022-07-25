import pandas


data = pandas.read_csv("50_states.csv")
# print(data)

states = data.state.tolist()
x_coord = data.x
y_coord = data.y


coords = {}
for state in states:
    coords[state] = []

# print(coords)
i = 0
for key in coords:
    coords[key].append(x_coord[i])
    coords[key].append(y_coord[i])
    i += 1
# print(coords)
