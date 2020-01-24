from pdf2image import convert_from_path
import os
import tempfile

os.chdir(r'')
filename=''

with tempfile.TemporaryDirectory() as path:
    images_from_path=convert_from_path(filename,output_folder=os.getcwd())
    
base_filename=os.path.splitext(os.path.basename(filename))[0]+'.jpg'

save_dir=os.getcwd()

for page in images_from_path:
    page.save(os.path.join(save_dir,base_filename),'JPEG')
