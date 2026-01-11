def multi_yield():
    yield_str = "This will print the first string"
    yield yield_str
    yield_str = "This will print the second string"
    yield yield_str

multi_obj = multi_yield()
print(next(multi_obj))

print(next(multi_obj))

try:
    print(next(multi_obj))
except:
    print("Exception on calling next after last yield was exhausted")

print(next(multi_obj, "End"))