---
layout: default
name: App This Competition
title: App This Competition
---

## New to CODATA?
Welcome! You've landed on the page describing CODATA's internal competition sponsored by [AppThis](https://appthis.com). If you are a newly-matriculated or incoming CU Boulder graduate student, or if you are an undergraduate student wanting to become more involved in CODATA, we strongly encourage you to sign up for a spot on our [Slack team](https://cubdatascienceteam.slack.com/). If you have an email ending in `colorado.edu`, you should be able to sign up with no issues, but if you do experience any technical difficulties, do not hesitate to send an email to codata@colorado.edu or bradley.gordon@colorado.edu.

Once you've signed up to join our Slack team, feel free to reach out to either `brad` or `pedro` if you have any questions at all.

## A Guide to the AppThis Competition

### What _is_ the AppThis Competition?
One of CODATA's goals is to provide team members with opportunities to demonstrate their ability to perform practical data science tasks. To this end, industry partners assist us by providing the team with a problem to solve and the data to solve that problem. For this competition, [AppThis](https://appthis.com) has generously allowed us to use their data to attempt to solve a problem central to their business model. More on that below. 

### What's at stake?
In addition to providing us with data and a problem to solve, AppThis has provided us with prizes to be awarded to teams with the best-performing models. The prizes are as follows: **First place: $500, Second place: $350, Third place: $150**. 

### What Problem is CODATA Solving?
AppThis is an adtech company, so much of their business model relies on building models that can accurately predict whether a user will click on one of their ads. The task for CODATA team members then is to build a model that can best determine whether a user will click on a particular ad. 

### What are the Data?
The data are JSON objects that represent user "events" on a mobile device, coupled with information about the "offer" presented to that user. You can think of an "offer" as an ad that, when clicked on by a user, redirects that user to an app store link to the landing page of a specific application. Models must use past user events to predict the probability that a user will click on an offer, or "convert." More technically, the training data can be thought of as tuples of the form, `(<user_event>, <converted>)`, where `<converted>` is 0 or 1. The validation dataset consists solely of user events, and for each event models must output a conversion probability. 

### How is Performance Measured?
As described above, models built by CODATA team members receive as input a series of user events and should output for each event the probability that user event represents a "conversion." One common metric for prediction tasks is the area under the curve or "AUC" metric. For the purposes of this competition, we use this metric to measure model performance. (Technically this metric should be called AUROCC, as we are measuring the area under the [Receiver Operating Characteristic curve](https://en.wikipedia.org/wiki/Receiver_operating_characteristic), but we adopt the shortened name AUC, which is the most popular way to refer to the metric.)

### I Want to Compete. What Should I Do?
The CODATA leadership team has developed its own leaderboard web application, which can be found [here](https://leaderboard.entilzha.io/). It's still pretty rough around the edges, so in order to compete you must first register for an account on the site, then ask via Slack or email either `brad` (bradley.gordon@colorado.edu) or `pedro` (p.rodriguez@colorado.edu) to add your user to a team (you can have a team of only one member). Once you are on a team, you can visit the AppThis competition leaderboard [page](https://leaderboard.entilzha.io/competition/appthis/) to make a submission.

### Where Are the Training Data?
[Click here](http://leaderboard.entilzha.io/static/downloads/all_test_data.tgz) to download all of the training data (~750MB).

### Any Hints?
Keep an eye on this page for more updates regarding the competition. The leadership team will post throughout the summer some notebooks on how to approach the competition. This will hopefully help members with less experience than others mount a worthwhile challenge. 
