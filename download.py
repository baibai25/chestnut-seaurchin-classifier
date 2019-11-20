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
    arguments = {'keywords': args.keywords, 'limit': args.limit, 'print_urls':True} # creating list of arguments
    paths = response.download(arguments)   # passing the arguments to the function
    print(paths)


if __name__ == '__main__':
    main()
