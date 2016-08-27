# Getting Started

These three links summarize the setup process. For full instructions refer to these.

1. https://help.github.com/articles/using-jekyll-as-a-static-site-generator-with-github-pages/
2. https://help.github.com/articles/about-github-pages-and-jekyll/
3. https://help.github.com/articles/setting-up-your-github-pages-site-locally-with-jekyll/

For quick instructions to get setup, do the following.

1. Clone repository with `git clone git@github.com:CoDataScience/codatascience.github.io.git --recursive`
2. Run `git submodule init`
3. Run `git submodule update`
4. Ensure you have Ruby 2.0 or higher installed with `ruby --version`
5. Run `gem install bundler`
6. Run `bundle install` (from the repository directory)
7. To run a local development version of the site run `bundle exec jekyll serve -w`

Any changes committed to master will trigger a rebuild and deploy of the website. Confirmation of the
commit and build status are posted in the `#github` channel on slack.

## Updating Notebooks

All the notebooks are obtained from git submodules that are in `_notebooks/repositories`. By convention any repository
in the data science team puts notebooks intended to be published on the website in `<ROOT>/notebooks` and no other files.

### Steps
1. Update the git submodules of interest by running `git pull` in the submodule directory then use `git add` and `git commit`
as you would add any other change to git.
2. `cd _notebooks` then run `./generate.py`
3. This results in new html markdown files that need to be committed as with any other file. This is necessary to make github pages work.



## Additional Info

Periodically we should run `bundle update github-pages` to update to the same versions that Github Pages uses

