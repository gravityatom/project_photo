# -*- coding: utf-8 -*-
import argparse
import pathlib


args = ' '



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
    
    
    
if __name__ == '__main__':
    
    main()
    
    
    
    
    