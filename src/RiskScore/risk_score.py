from scipy.stats import norm

class RiskScorer:


    def __init__(self):
        pass

    @classmethod
    def score_band(cls, risk):
        if risk < 40:
            return "Low Risk"
        elif 40 <= risk < 70:
            return "Medium Risk"
        elif 70 <= risk < 90:
            return "High Risk"
        else:
            return "Critical Risk"


    def compute_scores(self, data):
        if data is not None:

            numeric_cols = [
                'count_transaction', 'avg_amount', 'total_amount',
                'max_amount', 'daily_velocity_count', 'errorBalanceOrig'
            ]

            z_score_cols = []
            for col in numeric_cols:
                mean = data[col].mean()
                std = data[col].std()

                col_name = f'{col}_zscore'
                if std != 0:
                    z_val = (data[col] - mean) / std

                    data[col_name] = norm.cdf(z_val)
                else:
                    data[col_name] = 0
                z_score_cols.append(col_name)

            data['final_risk_score'] = data[z_score_cols].mean(axis=1) * 100
            data['risk_band']=data['final_risk_score'].apply(RiskScorer.score_band)

            return data

        else:
            raise ValueError ("Dataframe is empty or None!")