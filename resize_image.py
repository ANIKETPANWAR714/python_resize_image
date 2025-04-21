from PIL import Image
 
input_image_path = "input.jpg"      
output_image_path = "resized.jpg"  
 
 
with Image.open(input_image_path) as img:
     
     new_size = (400, 300)  
     resized_img = img.resize(new_size)
     resized_img.save(output_image_path)
 
print(f"Image resized and saved as {output_image_path}")