class SummaryConsole:
    def __init__(self):
        pass


    def summary_console(self,data):

        if data is not None:
            try:
                print("\n" + "=" * 30)
                print(">>>>>FRAUD ANALYSIS SUMMARY<<<<<")
                print("=" * 30)

                tot_transaction=len(data)
                tot_suspicious=data["is_suspicious"].sum()
                fraud_percentage = (tot_suspicious / tot_transaction) * 100

                print(f"Total Transactions: {tot_transaction:,}")
                print(f"Flagged as Suspicious: {tot_suspicious:,}")
                print(f"Alert Rate: {fraud_percentage:.2f}%")
                print("-" * 30)

                print(">>>>>Risk Level Distribution<<<<<")


                risk_counts = data['risk_band'].value_counts()
                for level, count in risk_counts.items():
                    print(f"   - {level}: {count:,}")

                print("-" * 30)


                print("Top 5 High-Risk Transactions:")

                top_5=data.sort_values(by="final_risk_score" , ascending=False).head(5)

                print(top_5[['nameOrig', 'amount', 'final_risk_score', 'risk_band']])


                print("-" * 30)


            except ValueError as e:
                print(e)
        else:
            raise ValueError ("Dataframe is empty or None!")


