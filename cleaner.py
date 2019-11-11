#!/usr/bin/env python3

import pandas as pd

file_in = input("Scrivi il path del questionario da pulire!   ")

raw = pd.read_csv(file_in)

useless_features = ['Status',
                    'IPAddress',
                    'Progress',
                    'Duration (in seconds)',
                    'RecordedDate',
                    'ResponseId',
                    'RecipientLastName',
                    'RecipientFirstName',
                    'RecipientEmail',
                    'ExternalReference',
                    'LocationLatitude',
                    'LocationLongitude',
                    'DistributionChannel',
                    'UserLanguage']

raw = raw.drop(useless_features, axis=1)
raw = raw.drop([0, 1], axis=0)

raw.to_csv('clean_' + file_in, index=False)
