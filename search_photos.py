# -*- coding: utf-8 -*-
import argparse
import pandas as pd

args = ' '

def search_photos(photo_db):   
    global args
   
    print("Inside search photos")
   
    df = pd.read_csv(photo_db)
    
    df.query('datetime == args.start_date' and 'datetime == args.end_date', inplace = True)
    print(df)














def main():
    global args
    
    # TODO: Can change later
    parser = argparse.ArgumentParser(description = "Search Photos") 
    
    # setting up the options : photodir, help, and build index 
    parser.add_argument("--start_date", type = str, required = True, 
                        help = "start date" )
    
    parser.add_argument("--end_date", type = str, required = True, 
                        help = "end date" )
    
    parser.add_argument("--photo_db", type = str, required = True, 
                        help = "photo database in csv format" )
   
    parser.add_argument("--h", help = "display help", action = "store_true")
    
    
    args = parser.parse_args()

    print(f"Searching images from {args.start_date} to {args.end_date}.")
    
    search_photos(args.photo_db)
    
if __name__ == '__main__':
    
    main()
    
    
    
    
    