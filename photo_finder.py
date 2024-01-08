# -*- coding: utf-8 -*-
import argparse

import pathlib

from PIL import Image

from PIL.ExifTags import TAGS


def find_photos(photo_dir):
   
    photo_count = 0 
   
    print(f"Searching for photos in {photo_dir}.")
    
    start_dir = pathlib.Path(photo_dir)
   
    for photo in start_dir.rglob("*.jpg"):
        
        print(f"Found photo: {photo}")
        
        photo_count += 1
       
        extract_metadata(photo)
    
    print(f"Photo count: {photo_count}.")
        


def extract_metadata(photo):
    
    print(f"Extracting metadata from {photo}.")
    
    # opens image
    image = Image.open(photo)
    
    # extracting the exif metadata
    exifdata = image.getexif()
    
    # looping through all the tags present in exifdata
    for tagid in exifdata:
   
        # getting the tag name instead of tag id
        tagname = TAGS.get(tagid, tagid)
        
        # passing the tagid to get its respcetive value
        value = exifdata.get(tagid)
        
        print(f"  {tagname:25}: {value}")
    
    
    

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
    
    
    
    
    