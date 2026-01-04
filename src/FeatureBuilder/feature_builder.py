import numpy as np
import pandas as pd


class FeatureBuilder:
    def __init__(self):
        pass

    def built_feature(self, data):
        if data is None or data.empty:
            raise ValueError("Dataframe is empty or None!")

        data["day"] = np.ceil(data["step"] / 24).astype(np.int32)

        orig_groups = data.groupby("nameOrig")["amount"]
        agg_stats = orig_groups.agg(['count', 'sum', 'mean', 'max', 'std'])
        agg_stats.columns = ["count_transaction", "total_amount", "avg_amount", "max_amount", "std_amount"]

        data = data.join(agg_stats, on="nameOrig")

        data["z_score"] = (data["amount"] - data["avg_amount"]) / data["std_amount"].replace(0, np.nan)

        data['daily_velocity_count'] = data.groupby(['nameOrig', 'day'])['amount'].transform('count')

        data['errorBalanceOrig'] = data['newbalanceOrig'] + data['amount'] - data['oldbalanceOrg']

        return data