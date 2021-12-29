from facebook_page_scraper import Facebook_scraper
import argparse

# create the scrap function with parameters (directory of the csv file, name of the facebook page, number of posts we want to scrap)
def scrap(directory,page_name,posts_count):
    # select the browser 
    browser = "chrome"

    # begin scraping
    posts = Facebook_scraper(page_name, posts_count, browser)
    # scrap to JSON
    data = posts.scrap_to_json()
    filename = page_name
    # convert to csv file
    posts.scrap_to_csv(filename, directory)
    return 'scrap is DONE'

# add command line arguments with argparse
parser = argparse.ArgumentParser(description='scrap facebook page by giving the name and the postes number')
parser.add_argument('directory', type=str, help='directory')
parser.add_argument('page_name', type=str,help='page name')
parser.add_argument('posts_count', type=int,help='posts number')
args = parser.parse_args()

if __name__=='__main__':
    print(scrap(args.directory,args.page_name, args.posts_count))