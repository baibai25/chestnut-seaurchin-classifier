import argparse
from google_images_download import google_images_download

def main():
    # parser
    parser = argparse.ArgumentParser()
    parser.add_argument('-k', '--keywords', help='Set keywords: e.g. key A, key B, key C')
    parser.add_argument('-l', '--limit', help='Number of images to download')
    args = parser.parse_args()
    
    # download images 
    response = google_images_download.googleimagesdownload()    # class instantiation
    
    # creating list of arguments
    arguments = {
        'keywords': args.keywords,
        'limit': args.limit,
        #'print_urls':True,
        'chromedriver': '/usr/bin/chromedriver'
    } 
    
    paths = response.download(arguments)   # passing the arguments to the function


if __name__ == '__main__':
    main()
