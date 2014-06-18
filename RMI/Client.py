import Pyro4

data = []
result = Pyro4.Proxy("PYRONAME:rmi")
data = result.getData()
for node in data:
    print node