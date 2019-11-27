#!/usr/bin/env python3

import pandas as pd



def remove_features(data):
    useless_features = ['StartDate',
                        'EndDate',
                        'Status',
                        'IPAddress',
                        'Progress',
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

    data = data.drop(useless_features, axis=1)
    data = data.drop([0, 1], axis=0)
    return data




if __name__ == '__main__':

    file_in = input("Scrivi il path del questionario da pulire: ")
    raw = pd.read_csv(file_in)
    new = remove_features(raw)
    new.to_csv('clean_' + file_in, index=False)
