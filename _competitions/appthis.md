---
layout: default
name: App This Competition
title: App This Competition
---

## Introduction and Quickstart Instructions

The first step is to download the tarball at [this link](leaderboard.entilzha.io/static/downloads/appthis.tgz) and to extract it using the Unix command `tar -xzvf appthis.tgz`, which will provide you with an `appthis` directory in the directory in which you ran the `tar` command.

The `appthis` directory represents the simplest setup we could provide to help you be successful
in this competition. Below is a quickstart list of steps to get your first model up and
running:
1) Install into your virtualenv of choice the requirements found in the requirements.txt
file (this should work with either Python 2.x or 3.x, though we recommend using 3.x):
    pip install -r requirements.txt
2) Run the script `train_and_score_model.py` in the following manner:
    python train_and_score_model.py training_data.tgz test_data.tgz my_preds.csv
where my_preds.csv can be any filename you want it to be, but the training_data.tgz and test_data.tgz
represent the names of the tarballs for the training and test data respectively, so you shouldn't
change those parameters unless you've renamed the tarballs for some reason.
3) That's it! The script you ran will produce a CSV of predicted conversion probabilities for the
events found in the test data, and the output of the command should also include the AUC and log loss
for the baseline model, which is found in `model.py`.


### How to Customize the Model Used in `train_and_score_model.py`

The model used in the entrypoint script `train_and_score_model.py` can be found in the `get_model`
method of the module `model.py`. If you want to create a custom model to fit the training data to
and to predict conversion probabilities for the events in the test data, the `get_model` method
is where you want to place that custom model. As it stands, the default baseline model is a vanilla
version of the sklearn.ensemble.GradientBoostingClassifier. It does not perform very well (it gets
~.5 AUC, which is just as good as guessing whether a given event in the test data eventually converted).

### About the Competition

Remember, the goal of the competition is to take user "events" (encoded as JSON objects in the
training_data.tgz and test_data.tgz archives) and predict the probability that those JSON objects
will "convert" (or will download the app detailed in the "offers" sections of the JSON events).
The AUC is a measure of how well your model predicts the probability of conversion.

Tips:
* Remember that the state of the art for this kind of modeling is logistic regression, and specifically
"follow the regularized leader" (FTRL) logistic regression (there are many papers written on the subject,
and even some software libraries you should check out).

* Also keep in mind that more recent events are more valuable from a modeling perspective than older events.
Whether that means you don't use older events, or you weight their contributions in the model less than more
recent events, is up to you, but the importance of recent events is something you should take into consideration
if you want to define a useful  model for click through rate (CTR).


### About the Other Parts of the Directory

In general, the `lib` directory within the parent `appthis` directory should not be tampered with, as it contains
files necessary to the successful execution of the entrypoint script `train_and_score_model.py`. Here is a quick
rundown of what each of the files in `lib` is meant to contribute:

`data.py`: This module contains a helper function that takes an argument a tarball (.tgz file) with test or training
data and emits events encoded as JSON objects. That function is called `data_iterator`.

`encoder.py`: This module contains a class called `VectorEncoder` whose purpose is to take a JSON-encoded event emitted
by the `data_iterator` function (or generator) defined above and to encode it as a numerical vector. The details of how
it does this are present in that file. Essentially it treats numerical feature values as floats, and it hashes categorical
feature values so that all the features end up being numeric and therefore more easily digested by sklearn models.

`feature_defs.py`: The `VectorEncoder` class introduced above in the description of the `encoder.py` module uses these
feature definitions to know which features are categorical and which features are numeric in nature. If you want to know
more about the features contained in each event JSON object, consult this module. The features themselves have pretty
informative names. Remember that feature selection will also be an important part of an effective modeling strategy.

`test_labels.txt`: These are the "ground truth" labels of the events provided in the test_data.tgz tarball.

`scoring.py`: This simple module uses the labels in `test_labels.txt` to determine the accuracy of your model's predicted
conversion probabilities by applying the AUC (or, more accurately, the AUROC) metric to the predictions CSV generated by
`train-and_score_model.py`.


That's it! Happy modeling!
