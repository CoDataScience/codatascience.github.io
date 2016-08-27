#!/usr/bin/env python3

import os
import subprocess


def shell(command):
    subprocess.run(command, shell=True, check=True)


def list_notebooks():
    repositories = os.listdir('repositories')
    pairs = []
    for r in repositories:
        pairs.extend([(r, notebook.split('.')[0]) for notebook in os.listdir('repositories/{repository}/notebooks'.format(repository=r))])
    return pairs


def convert(repository, notebook):
    shell('jupyter nbconvert --output ../../../{repository}/{notebook}_tmp.html repositories/{repository}/notebooks/{notebook}.ipynb'.format(
        repository=repository, notebook=notebook)
    )
    with open('{repository}/{notebook}_tmp.html'.format(repository=repository, notebook=notebook)) as tmp:
        with open('{repository}/{notebook}.md'.format(repository=repository, notebook=notebook), 'w') as f:
            f.write('---\nlayout: raw\ntitle: {notebook} in {repository}\nrepository: {repository}\n---\n'.format(
                repository=repository, notebook=notebook))
            first = True
            for line in tmp:
                if first:
                    first = False
                    continue
                else:
                    f.write(line)
    shell('rm {repository}/{notebook}_tmp.html'.format(repository=repository, notebook=notebook))


if __name__ == '__main__':
    pairs = list_notebooks()
    for repository, notebook in pairs:
        convert(repository, notebook)

