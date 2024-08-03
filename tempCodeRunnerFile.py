s=[([[1]+[0]*(n-1)])*(n-1)]
kernel=[list(map(int,f.split()))]+flat(s)
kernel=flatten(kernel)