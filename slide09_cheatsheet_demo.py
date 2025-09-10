"""Quick sampler of common list ops for live typing."""
xs = [10, 20, 30]
print("index 1:", xs[1]) # read by spot
xs.append(40) # add at end
print("after append:", xs)
print("slice 1:3:", xs[1:3]) # makes a copy