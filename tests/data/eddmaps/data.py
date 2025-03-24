#!/usr/bin/env python3

# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import pandas as pd

filename = 'mappings.csv'

size = 3
data = {
    'gbifID': [''] * size,
    'decimalLatitude': [41.881832] * size,
    'decimalLongitude': [''] + [-87.623177] * (size - 1),
    'objectid': [''] * size,
    'reporter': [''] * size,
    'RecOwner': [''] * size,
    'SciName': ['Homo sapiens'] * size,
    'ComName': ['human'] * size,
    'Nativity': ['Native'] * size,
    'OccStatus': ['Detected'] * size,
    'Status': ['Positive'] * size,
    'ObsDate': ['', '', '05-07-22'],
    'DateEnt': ['05-07-22'] * size,
    'DateUp': ['05-07-22'] * size,
    'Location': ['Chicago, Illinois, United States'] * size,
    'Latitude': [41.881832] * size,
    'Longitude': [''] + [-87.623177] * (size - 1),
    'Datum': ['WGS84'] * size,
    'Method': [''] * size,
    'CoordAcc': [''] * size,
    'DataType': [''] * size,
    'Centroid': [''] * size,
    'Abundance': [''] * size,
    'InfestAcre': [''] * size,
    'GrossAcre': [''] * size,
    'Percentcov': [''] * size,
    'Density': [''] * size,
    'Quantity': [''] * size,
    'QuantityU': [''] * size,
    'APPXQuant': [''] * size,
    'NumCollect': [''] * size,
    'Smallest': [''] * size,
    'Largest': [''] * size,
    'Incidence': [''] * size,
    'Severity': [''] * size,
    'Host': [''] * size,
    'Host_Name': [''] * size,
    'HostPheno': [''] * size,
    'HostDamage': [''] * size,
    'ManageStat': ['Unknown'] * size,
    'PopStat': [''] * size,
    'Habitat': [''] * size,
    'LocalOwner': [''] * size,
    'Site': [''] * size,
    'RecBasis': [''] * size,
    'Museum': [''] * size,
    'MuseumRec': [''] * size,
    'Voucher': [''] * size,
    'ObsIDer': [''] * size,
    'CollectTme': [''] * size,
    'UUID': [''] * size,
    'OrgSrcID': [''] * size,
    'OrigName': ['Homo sapiens'] * size,
    'RecSrcTyp': ['Bulk Data'] * size,
    'Surveyor': [''] * size,
    'DateAcc': [''] * size,
    'VisitType': [''] * size,
    'DataMthd': [''] * size,
    'TrapType': [''] * size,
    'NumTraps': [''] * size,
    'TargetName': [''] * size,
    'TargetCnt': [''] * size,
    'TargetRnge': [''] * size,
    'Phenology': [''] * size,
    'LifeStatus': [''] * size,
    'Sex': [''] * size,
    'PID': [''] * size,
    'WaterName': [''] * size,
    'WaterType': [''] * size,
    'Substrate': [''] * size,
    'TreatArea': [''] * size,
    'PlantTreat': [''] * size,
    'TreatComm': [''] * size,
    'Reference': [''] * size,
    'Locality': [''] * size,
    'Comments': [''] * size,
    'ReviewDate': ['05-07-22'] * size,
    'Reviewer': ['Charles Darwin'] * size,
    'VerifyMthd': ['Bulk Verified'] * size,
    'Verified': ['Verified'] * size,
    'IDCred': ['Credible'] * size,
    'ReviewComm': [''] * size,
}

df = pd.DataFrame(data)
df.to_csv(filename, index=False)
