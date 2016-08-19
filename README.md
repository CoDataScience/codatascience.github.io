# Getting Started

These three links summarize the setup process. For full instructions refer to these.

1. https://help.github.com/articles/using-jekyll-as-a-static-site-generator-with-github-pages/
2. https://help.github.com/articles/about-github-pages-and-jekyll/
3. https://help.github.com/articles/setting-up-your-github-pages-site-locally-with-jekyll/

For quick instructions to get setup, do the following.

1. Clone repository with `git clone git@github.com:CoDataScience/codatascience.github.io.git`
2. Ensure you have Ruby 2.0 or higher installed with `ruby --version`
3. Run `gem install bundler`
4. Run `bundle install` (from the repository directory)
5. To run a local development version of the site run `bundle exec jekyll serve -w`

Any changes committed to master will trigger a rebuild and deploy of the website. Confirmation of the
commit and build status are posted in the `#github` channel on slack.

## Additional Info

Periodically we should run `bundle update github-pages` to update to the same versions that Github Pages uses



