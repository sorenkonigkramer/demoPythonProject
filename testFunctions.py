def getRiskWeights(riskType, subRiskType):
    riskeWeightsVec =''
    if riskType == 'InterestRate':
        if subRiskType == 'RegularCurrencies':
            riskeWeightsVec = [114, 107, 95, 71, 56, 53, 50, 51, 53, 50, 54, 63]
        elif subRiskType == 'LowVolatilityCurrencies':
            riskeWeightsVec = [15, 21, 10, 10, 11, 15, 18, 19, 19, 18, 20, 22]
        elif subRiskType == 'HighVolatilityCurrencies':
            riskeWeightsVec = [103, 96, 84, 84, 89, 87, 90, 89, 90, 99, 100, 96]
        else:
            print('Error subRiskTypeUndefined')
        print(f'Still need to develop inflation rate and x-currency risk weights')
    elif riskType == 'CreditQualifying':
        riskeWeightsVec = [75, 89, 68, 51, 50, 47, 157, 333, 142, 214, 143, 160, 333]
    elif riskType == 'CreditNonQualifying':
        riskWeightsName = ['Bucket 1', 'Bucket 2', 'Residual']
        riskeWeightsVec = [240, 1000, 1000]
    elif riskType == 'Equity':
        riskeWeightsVec = [23, 25, 29, 26, 20, 21, 24, 24, 29, 28, 15, 15, 29]
    elif riskType == 'Commodity':
        riskeWeightsVec = [16, 20, 23, 18, 28, 18, 17, 57, 21, 39, 20, 20, 15, 15, 11, 57, 16]
    elif riskType == 'FX':
        riskeWeightsVec = [7.5, 7.5, 7.5, 7.5]
    else:
        print('Error Risk Type Undefined')
    return riskeWeightsVec


def getRiskWeightNames(riskType):
    riskWeightsName = ''
    if riskType == 'InterestRate':
        riskWeightsName = ['2w', '1m', '3m', '6m', '1yr', '2yr', '3yr', '5yr', '10yr', '15yr', '20yr', '30yr']
        print(f'Still need to develop inflation rate and x-currency risk weights')
    elif riskType == 'CreditQualifying':
        riskWeightsName = ['Bucket 1', 'Bucket 2', 'Bucket 3', 'Bucket 4', 'Bucket 5', 'Bucket 6', 'Bucket 7',
                           'Bucket 8', 'Bucket 9', 'Bucket 10', 'Bucket 11', 'Bucket 12', 'Residual']
    elif riskType == 'CreditNonQualifying':
        riskWeightsName = ['Bucket 1', 'Bucket 2', 'Residual']
    elif riskType == 'Equity':
        riskWeightsName = ['Bucket 1', 'Bucket 2', 'Bucket 3', 'Bucket 4', 'Bucket 5', 'Bucket 6', 'Bucket 7',
                           'Bucket 8', 'Bucket 9', 'Bucket 10', 'Bucket 11', 'Bucket 12', 'Residual']
    elif riskType == 'Commodity':
        riskWeightsName = ['Bucket 1', 'Bucket 2', 'Bucket 3', 'Bucket 4', 'Bucket 5', 'Bucket 6', 'Bucket 7',
                           'Bucket 8', 'Bucket 9', 'Bucket 10', 'Bucket 11', 'Bucket 12', 'Bucket 13', 'Bucket 14',
                           'Bucket 15', 'Bucket 16', 'Bucket 17']
    elif riskType == 'FX':
        riskWeightsName = ['GivenRegularCalculationRegular', 'GivenHighCalculationRegular',
                           'GivenRegularCalculationHigh', 'GivenHighCalculationHigh']
    else:
        print('Error Risk Type Undefined')

    return riskWeightsName


def getRiskWithinBucketCorrelations(riskType, subRiskType):
    withinBucketNameVec =''
    withinBucketCorrelation = ''
    if riskType == 'InterestRate':
        withinBucketNameVec= 'None'
        withinBucketCorrelation = []
        print(f'Still need to develop inflation rate and x-currency risk weights')

    elif riskType == 'CreditQualifying':
        withinBucketNameVec = ['AggregateSame', 'AggregateDifferent', 'ResidualSame', 'ResidualDifferent']
        withinBucketCorrelation = [0.94, 0.42, 0.5, 0.5]
    elif riskType == 'CreditNonQualifying':
        withinBucketCorrelation = ['AggregateSame', 'AggregateDifferent', 'ResidualSame', 'ResidualDifferent']
        withinBucketCorrelation = [0.77, 0.47, 0.5, 0.5]
    elif riskType == 'Equity':
        withinBucketNameVec = getRiskWeightNames('Equity')
        withinBucketCorrelation = [0.14, 0.2, 0.28, 0.23, 0.18, 0.29, 0.34, 0.3, 0.19, 0.17, 0.41, 0.41, 0]
    elif riskType == 'Commodity':
        withinBucketNameVec = getRiskWeightNames('Commodity')
        withinBucketCorrelation = [0.16, 0.98, 0.77, 0.82, 0.98, 0.89, 0.96, 0.48, 0.64, 0.39, 0.45, 0.53, 0.65,
                                   0.12, 0.21]
    elif riskType == 'FX':
        withinBucketNameVec = getRiskWeightNames('FX')
        withinBucketCorrelation = [0.5, 0.5, 0.5, 0.5]
    else:
        print('Error Risk Type Undefined')


def getRiskBetweenBucketCorrelations(riskType, subRiskType):
    print('To be developed')