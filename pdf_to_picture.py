from pdf2image import convert_from_path
import os
import tempfile

os.chdir(r'C:/Users/Thierry/Desktop/test-no')
filename='hawsco-dec-2018-43332-t.pdf'

with tempfile.TemporaryDirectory() as path:
    images_from_path=convert_from_path(filename,output_folder=os.getcwd())
    
base_filename=os.path.splitext(os.path.basename(filename))[0]+'.jpg'

save_dir=os.getcwd()

for page in images_from_path:
    page.save(os.path.join(save_dir,base_filename),'JPEG')
