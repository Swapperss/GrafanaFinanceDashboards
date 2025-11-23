#creating rules to identify transactions
def run_rules(df):
    
    df['rules_triggered'] = None
    df['rules_explanation'] = None
    df['decision'] = None

    if df['amount'][0] >= 100 and df['account_blacklisted'][0]==False and df['trans_type'][0]=='Real_time_transaction':
        df['rules_triggered'] = 'Rule1'
        df['rules_explanation'] = 'User is trying to make a transaction of more than 100$'
        df['decision'] = 'Rejected'

    elif df['account_blacklisted'][0] ==  df['trans_type'][0]=='Real_time_transaction':
        df['rules_triggered'] = 'Rule2'
        df['rules_explanation'] = 'It is a blacklisted Card'
        df['decision'] = 'Rejected'

    elif df['trans_type'][0]!='Real_time_transaction':
        df['rules_triggered'] = 'No Rules Triggered'
        df['decision'] = 'Approved'      
          
    else:
         df['rules_triggered'] = 'No Rules Triggered'

    dict_index = df.to_dict(orient='index')
    dict_single_row = dict_index[list(dict_index.keys())[0]]

    return dict_single_row