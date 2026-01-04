class TransactionFlagger:
    def __init__(self):
        pass

    def is_suspicious(self,data):

        if data is not None:
            data["is_suspicious"]=data["risk_band"].isin(["High Risk","Critical Risk"])
            return data


        else:
             raise ValueError("Dataframe is empty or None!\n")