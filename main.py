#!/usr/bin/python3

import logging
import argparse
import os
import re
import json
from github import Github


def main(args:argparse.ArgumentParser):
    logging.info('Looking up repo: %s' % args.repo)
    g = Github(args.token)
    r = g.get_repo(args.repo)
    labels = []
    response = []
    for issue in r.get_issues(state="open"):
        if len(issue.labels)>0:
            # Filter for uniques with a set
            labels = list(set(issue.labels + labels))
    for label in labels:
        response.append(label.name)

    print(json.dumps(response))



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-d', '--debug',
        help="Print debugging statements",
        action="store_const",
        dest="logLevel",
        const=logging.DEBUG,
        default=logging.WARNING
    )
    parser.add_argument(
        '-v', '--verbose',
        help="Print all info statements",
        action="store_const",
        dest="logLevel",
        const=logging.INFO
    )

    parser.add_argument(
        '-r', '--repo',
        help="Repo you are searching for in the format owner/repo_name",
        dest="repo",
        required=True
    )

    parser.add_argument(
        '-t', '--token',
        help="Personal access token to github. See https://tinyurl.com/54wkjtej",
        dest="token",
        default=os.getenv('GITHUB_TOKEN')
    )
    args = parser.parse_args()
    logging.basicConfig(level=args.logLevel)
    while not re.match("^[a-z0-9-]+\/[a-z0-9_\-.]+",args.repo):
        logging.warning("Repo is not in the correct format - owner/repo")
        args.repo = input("Enter the repo: ")

    while args.token is None or len(args.token) < 1:
        logging.warning("No Token provided or found in environment variables")
        args.token = input("Enter your Github personal access token: ")

    main(args)
