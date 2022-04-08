# -*- coding: utf-8 -*-
import pandas as pd
from datetime import datetime, timedelta
from googleapiclient.discovery import build

def get_activities_as_dataframe(creds, application_name, date):
    with build('admin', 'reports_v1', credentials=creds) as service:
        start_time = datetime.strptime(date, "%Y-%m-%d")
        end_time = start_time + timedelta(days=1)
        results = service.activities().list(userKey='all', applicationName=application_name, startTime=start_time.isoformat()+"Z", endTime=end_time.isoformat()+"Z").execute()
        activities = results.get('items', [])
        df = pd.DataFrame(pd.json_normalize(activities))
        return df
