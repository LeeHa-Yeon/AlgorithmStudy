x = ['Tick', 'Tock', 'Song']
y = ['Ping', 'Pong']
x.append(y)
print('append x:', x)

x = ['Tick', 'Tock', 'Song']
y = ['Ping', 'Pong']
x.extend(y)
print('extend x:', x)

# append x: ['Tick', 'Tock', 'Song', ['Ping', 'Pong']]
# extend x: ['Tick', 'Tock', 'Song', 'Ping', 'Pong']

x = ['Tick', 'Tock', 'Song']
y = [['Ping', 'Pong']]
x.append(y)
print('append x:', x)

x = ['Tick', 'Tock', 'Song']
y = [['Ping', 'Pong']]
x.extend(y)
print('extend x:', x)

# append x: ['Tick', 'Tock', 'Song', [['Ping', 'Pong']]]
# extend x: ['Tick', 'Tock', 'Song', ['Ping', 'Pong']]


x = ['Tick', 'Tock', 'Song']
y = 'Ping'
x.append(y)
print('append x:', x)

x = ['Tick', 'Tock', 'Song']
y = 'Ping'
x.extend(y)
print('extend x:', x)

# append x: ['Tick', 'Tock', 'Song', 'Ping']
# extend x: ['Tick', 'Tock', 'Song', 'P', 'i', 'n', 'g']