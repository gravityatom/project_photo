# -*- coding: utf-8 -*-
import argparse
import pathlib

def find_photos(photo_dir):
    print(f"Searching for photos in {photo_dir}.")
    start_dir = pathlib.Path(photo_dir)
    for photo in start_dir.rglob("*.jpg"):
        print(f"Found photo: {photo}")
        

def main():
   # TODO: Can change later
    parser = argparse.ArgumentParser(description = "Photo finder") 
    
    # setting up the options : photodir, help, and build index 
    parser.add_argument("--photo_dir", type = str, required = True, 
                        help = "photo directory" )
    
    parser.add_argument("--h", help = "display help", action = "store_true")
    
    parser.add_argument("--build_index", help = "build index from scratch", 
                        action = "store_true" )
    
    args = parser.parse_args()

    print(f"Processing {args.photo_dir} in your directory.")
    
    find_photos(args.photo_dir)
    
    
if __name__ == '__main__':
    main()