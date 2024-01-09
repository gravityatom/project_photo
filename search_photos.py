# -*- coding: utf-8 -*-
import argparse
import pathlib


args = ' '


    global args
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
    print(args.photo_db)
    f = open(args.photo_db, "w")
    f.write(csv_content)
    f.close()
        
    print(f"Photo count: {photo_count}.
    
    print(f"Extracting metadata from {photo}.")
       
   
   
    with open(photo, 'rb') as img_file:
        img = Image(img_file)
        

    print(f"make:{img.get('make')}")
     
    
    csv_row = f'{photo},'
    csv_row += f'{img.get("make")}'
    csv_row += f'{img.get("datetime")}'
    csv_row += f'{img.get("model")}'
    csv_row += "\n"

   
    return csv_row


def main():
    
    
    # TODO: Can change later
    parser = argparse.ArgumentParser(description = "Search Photos") 
    
    # setting up the options : photodir, help, and build index 
    parser.add_argument("--start_date", type = str, required = True, 
                        help = "start date" )
    
    parser.add_argument("--end_date", type = str, required = True, 
                        help = "end date" )
    
    parser.add_argument("--h", help = "display help", action = "store_true")
    
    
    args = parser.parse_args()

    print(f"Searching images from {args.start_date} to {args.end_date}.")
    
    find_photos(args.photo_dir)
    
    
if __name__ == '__main__':
    
    main()
    
    
    
    
    