from PIL import Image
import os

MAX_WIDTH = 1200

def proccess_image(path):

  try:
    with Image.open(path) as img:

      img.load()
      img.show()

      width, height = img.size
      print(width, height )

      if width > MAX_WIDTH:
        new_w = MAX_WIDTH
        new_h = int(height * (new_w / width))
        new_img = img.resize((new_w, new_h), Image.LANCZOS)
      new_img.show()

  except:
    print('ошибка')

def main():
  script_dir = os.path.dirname(__file__)
  images_path = os.path.join(script_dir, 'images')

  if not os.path.isdir(images_path):
    print('Такой папки нет')
    return
  
  files = sorted([os.path.join(images_path, f) for f in os.listdir(images_path) if os.path.isfile(os.path.join(images_path, f))])[1:]
  
  # добавить создание out
  print(files)

  for file in files:
    proccess_image(file)

if __name__ == '__main__':
  main()