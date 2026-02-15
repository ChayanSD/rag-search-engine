#!/usr/bin/env python3

import argparse
from lib.keyword_search import (search_command
, build_command , tf_command , idf_command , tfidf_command)
def main() -> None:
    parser = argparse.ArgumentParser(description="Keyword Search CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    search_parser = subparsers.add_parser("search", help="Search movies using BM25")
    search_parser.add_argument("query", type=str, help="Search query")
    
    tf_parser = subparsers.add_parser("tf", help="Get term frequency for a document")
    tf_parser.add_argument("doc_id", type=int, help="Document id to check")
    tf_parser.add_argument("term", type=str, help="Search Term to count for")
    
    subparsers.add_parser("build", help="Build the inverted index")

    search_parser = subparsers.add_parser("idf" , help="Calculate inverse document frequency")
    search_parser.add_argument("term", type=str, help="Search Term to count for")

    search_parser = subparsers.add_parser("tfidf" , help="Calculate tf-idf score")
    search_parser.add_argument("doc_id", type=int, help="Document id to check")
    search_parser.add_argument("term", type=str, help="Search Term to count for")

    args = parser.parse_args()

    match args.command:
        case "build":
            print("Building inverted index...")
            build_command()
            print("Inverted index built successfully.")
        case "search":
            print(f"Searching for: {args.query}")
            results = search_command(args.query, 5)
            for i , result in enumerate(results):
                print(f"{i} {result['title']}")
        case "tf":
            tf_command(args.doc_id, args.term)
        case "idf":
            idf_command(args.term)
        case "tfidf":
            tfidf_command(args.doc_id, args.term)
        case _:
            parser.print_help()


if __name__ == "__main__":
    main()