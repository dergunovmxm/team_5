from PIL import Image
import os

MAX_WIDTH = 1200

def proccess_image(path, script_dir=os.path.dirname(__file__)):

  try:
    with Image.open(path) as img:
      global MAX_WIDTH
      img.load()
      
      
      width, height = img.size
      #print(width, height )

      if width > MAX_WIDTH:
        new_w = MAX_WIDTH
        new_h = int(height * (new_w / width))
        new_img = img.resize((new_w, new_h), Image.LANCZOS)
        
      else:
        
        new_img = img
      #save = os.path.join(script_dir, output)
      out_path = os.path.join(script_dir, 'output')
      if not os.path.isdir(out_path):
        os.makedirs(out_path, exist_ok=True)
      filename = os.path.basename(path)
      name, ext = os.path.splitext(filename)
      save_filename = f"{name}_processed{ext}"
      save_path = os.path.join(out_path, save_filename)

      
      new_img.save(save_path)
    return script_dir
      
      

  except:
    print('ошибка')

def main():
  script_dir = os.path.dirname(__file__) #путь до скрипта
  images_path = os.path.join(script_dir, 'images')
  
  if not os.path.isdir(images_path):
    print('Такой папки нет')
    return
  
  files = sorted([os.path.join(images_path, f) for f in os.listdir(images_path) if os.path.isfile(os.path.join(images_path, f))])[1:]
  
  # добавить создание out
  print(files)

  for file in files:
    proccess_image(file, script_dir)
    
if __name__ == '__main__':
  main()
