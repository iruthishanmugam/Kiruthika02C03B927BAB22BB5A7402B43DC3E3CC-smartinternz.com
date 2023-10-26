def linearsearchproduct(Productlist,targetproduct):
  indices=[]
  for i,product in enumerate(Productlist):
    if product==targetproduct:
      indices.append(i)
  return indices
products=["apple","banana","apple","orange","apple"]
target="apple"
result=linearsearchproduct(products,target)
if result:
  print(f"The Product'{target}'was found at indices:{result}")
else:
  print(f"The product'{target}'was not found in the list.")