from PIL import Image

while True:
  path = input("Path to image file to convert (; to exit): ")
  if path == ";":
    break
  path.replace("/", r"\\")
  try:
    img = Image.open(path)
    img.save(path[path.rfind(r"\\")+1:path.rfind(".")-1] + ".ico", format="ICO", sizes=[(64, 64)])
  except (FileNotFoundError, AttributeError) as err:
    print(err)

print("Runtime ending...")
