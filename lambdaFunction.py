from datetime import datetime

def lambda_handler(event, context):
    now = datetime.now()
    print("date and time =", now.strftime("%d/%m/%Y %H:%M:%S"))
