---
layout: default
name: Oracle Data Cloud
---

<div class="row"><div class="col-md-4 col-md-offset-4"><img src="/images/competition/oracle.png" height="100"></div></div>

# Oracle Data Cloud Audience Competition

In this competition your objective is to use prior purchase data to maximize future revenue.

Suppose you are run a company called SuperMegaCorp which has enough money to send 100,000 advertisements per month to prospective customers. Your database has tens of millions of customers, but for each month you only look at roughly 1 million customers before deciding which 100,000 you send advertisements to.

## Data and Task Description

Each row of the data represents one "household". You can think of this as a representation of all the people and devices which live at a certain address. Each row contains a vector of sparse features representing data such as past transactional behavior and demographics. More details about these features may be provided, but for now this is all you know. Finally, each row contains the amount of money spent by the household in response to advertising.

### Data

You are provided four files for this competition:

* `train_set.tar.gz`: Training data which contains data from 2016-03-01 to 2016-04-30
* `val_set.tar.gz`: Validation data which contains data from 2016-05-01 to 2016-06-30
* `contest_set.tar.gz`: Contest data which contains data from 2016-07-01 to 2016-08-30. This does not have labels
* `total_spend.tar.gz`: Amount spent per household in the training and validation sets. This is provided for convenience.

**Obtaining Data**: To obtain the data please join our slack channel. If you don't know how to do so please send an email to `p.r?driguez@c?l?rad?.edu` substituting `?` with `o`

#### General Data Format

Each file is a compressed gzip archive which can be decompressed using `tar -xzvf file.tar.gz` The directory will contain a number of files named `part-00000.bz2`, `part-00001.bz2`, and so on. These can be decompressed using `bzip2 -d *.bz2`. You can merge everything into a single file using `cat *.bz2 > everything.txt`

#### Training and Validation File Format

Each row contains the household id, the amount spent by the household, the total number of features (constant across everything) and the sparse vector of features. Below is each feature labeled and an example

```
u’(<household id>, <spend>, (<total features>, [(<feature idx>, <feature value>), …]))'

u’(36839559, 0.0, (133531, [(0, 0.0040397762585456807), (144, 0.031645569620253167),…]))'

```

#### Total Spend File Format

For convenience the spend per household is also included in case you plan on training on a random subsample of the dataset. Labels are included for everything in the training and validation sets. Each row contains elements like below:

```
<household id>, <lifetime spend>
```

#### Contest File Format

This is identical to the training and validation except spend is always 0.

#### Description

Labels are provided in both the training and validation sets. The intent is to use the training set to train your models and the validation set to validate them. The validation is similar to what a leaderboard would be based on. The contest set will be used for final judging and has all 0s instead of labels.

Each of the training and validation sets contains a random sample of ~1,000,000 households which did not respond to ads and ~100,000 that did respond to ads. In general there won't be any or hardly any households between data sets. The following information may be helpful:

* When the spend value is greater than zero this indicates the household is a buyer
* If you do not advertise to a customer, that customer will not purchase anything (eg zero revenue)
* If you choose to advertise to a customer it is assumed that all of the spend is due to the ad
* In general households are unique across data sets

## Evaluation Metrics

This competition will award prizes according to two error metrics with additional prizes for secondary goals as listed below. In the primary evaluation metrics of revenue and number of buyers you will submit one model for both which identifies 100,000 households to advertise to.

### Submission Format

You will provide a submission in the following format named `<team_name>.csv`:

```
household_id,advertise
241239,5
1242350,4
109539,0
534309,0
1398304,0
1231,3
1231541,2
474564,1
```

The household id should match the contest data set. The advertise column should contain exactly 100,000 non-zeros and all zeros besides that. A non-zero indicates you would like to advertise to this household and its relative rank where a 1 indicates most desirable to advertise to. A 0 indicates you do not want to advertise to this household. The order is useful but is not part of the formal evaluation.

### Maximum Revenue in 100,000

Assume that $$A_i$$ is 1 if you decide to advertise to household $$i$$. Further assume that $$S_i$$ is the amount spent by household $$i$$ if it is advertised to. With these definitions the quantity to maximize is revenue $$R$$ defined as:

$$
R=\sum_{i\in\text{household ids}}A_iR_i
$$

### Most Number of Buyers in 100,000

To define this metric we introduce a variable $$I_i$$ which is equal to 1 if $$S_i>0$$ and 0 otherwise. With this definition the quantity to maximize is number of buyers $$B$$ defined as

$$
B=\sum_{i\in\text{household ids}}A_iI_i
$$

### Secondary Prizes

#### Fast and Accurate Model

In addition to the metrics above there will also be a prize awarded to a well performing and fast model. A separate submission is allowed for this and details will be given soon. In general though we expect your model to:

* Perform acceptably worse than competitive models with respect to $$R$$
* Train and Score on a beefy laptop or small server (4-8 cores 16-32GB of RAM) in less than a few hours at most

#### Creativity

In addition to prizes above there will also be a prize for creativity. This is obviously subjective, but creative visualizations and analysis of the data are highly encouraged.

## Prize Breakdown

### Revenue

* 1st Place \$200
* 2nd Place \$100

### Buyers

* 1st Place \$125
* 2nd Place \$75

### Fast and Accurate Model

* 1st Place \$50

### Creativity

* 1st Place \$50

## Additional Rules

* To receive prizes all code must be licensed under the Apache V2.0 License
* Model training and scoring should be independently reproducible
* Competition will end November 13th
* A custom leaderboard may be provided partway through the competition as a progress check
* Additional prizes may be announced at a later date
* To compete and receive prizes you must be affiliated with CU Boulder or have been recently associated with CU Boulder (eg. recent grad)
* There is no strict limit on team sizes, but prizes are per team not per person.

