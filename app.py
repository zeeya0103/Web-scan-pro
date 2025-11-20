from crawler import run_crawler
from auth_test import authenticate
from generate_docs import generate_document

def main():
    authenticate()
    run_crawler()
    generate_document()

if __name__ == "__main__":
    main()
