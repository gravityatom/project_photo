# -*- coding: utf-8 -*-
import argparse




def main():
   # TODO: Can change later
    parser = argparse.ArgumentParser(description = "Photo finder") 
    
    # setting up the options : photodir, help, and build index 
    parser.add_argument("--photo_dir", type = str, required = True, 
                        help = "photo_directory" )
    
    parser.add_argument("--h", help = "display help" )
    
    parser.add_argument("--build_index", help = "build index from scratch" )
    
    args = parser.parse_args()



if __name__ == ' __main__':
    main()