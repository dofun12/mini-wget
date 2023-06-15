from libs.urlutils import Downloader
import argparse

parser = argparse.ArgumentParser(description='Download file from url')
parser.add_argument('url', help='Download Url')
parser.add_argument('-o', dest='output_file', action='store',
                    help='Set the outputfile', required=True)

args = parser.parse_args()

url: str = args.url
outfile_path: str = args.output_file

if not (url.startswith('http://') or url.startswith('https://')):
    print('Not a valid url')
    exit(1)

dowloader = Downloader()
dowloader.download_url(url, outfile_path)
