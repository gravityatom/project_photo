# -*- coding: utf-8 -*-
import argparse




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



if __name__ == '__main__':
    main()