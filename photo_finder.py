# -*- coding: utf-8 -*-
import argparse

import pathlib

from exif import Image


def find_photos(photo_dir):
   
    photo_count = 0 
   
    csv_content = "photo,make,datetime,model\n"
   
    print(f"Searching for photos in {photo_dir}.")
    
    start_dir = pathlib.Path(photo_dir)
   
    for photo in start_dir.rglob("*.jpg"):
        
        print(f"Found photo: {photo}")
        
        photo_count += 1
       
        
       
        photo_metadata = extract_metadata(photo)
        
        # append row to csv_content
        csv_content += photo_metadata
        
        

    # saving csv_content to a file
    f = open(args.photo_db, "w")
    f.write(csv_content)
    f.close()
        
        
        
    print(f"Photo count: {photo_count}.")
        


def extract_metadata(photo):
    
    print(f"Extracting metadata from {photo}.")
       
   
    # opens image
    #image = Image.open(photo)
    with open(photo, 'rb') as img_file:
        img = Image(img_file)
        
    
    csv_row = f"{photo},{img.get("make")},{img.get("datetime")},{img.get("model")}\n"
    return csv_row
    #print(f"{img.list_all()}")

    
    


def main():
    # TODO: Can change later
    parser = argparse.ArgumentParser(description = "Photo finder") 
    
    # setting up the options : photodir, help, and build index 
    parser.add_argument("--photo_dir", type = str, required = True, 
                        help = "photo directory" )
    
    parser.add_argument("--photo_db", type = str, required = True, 
                        help = "photo database in csv format" )
    
    parser.add_argument("--h", help = "display help", action = "store_true")
    
    parser.add_argument("--build_index", help = "build index from scratch", 
                        action = "store_true" )
    
    args = parser.parse_args()

    print(f"Processing {args.photo_dir} in your directory.")
    
    find_photos(args.photo_dir)
    
    
if __name__ == '__main__':
    
    main()
    
    
    
    
    