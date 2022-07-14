from PIL import Image

while True:
  path = input("Path to image file to convert (; to exit): ")
  if path == ";": break
  path.replace("/", "\\")
  try:
    img = Image.open(path)
    img.save(f'{path[path.rfind("\\")+1:]}.ico')
  except (FileNotFoundError, AttributeError) as err:
    print(err)

print("Runtime ending...")
