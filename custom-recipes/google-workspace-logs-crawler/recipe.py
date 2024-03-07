# -*- coding: utf-8 -*-
import dataiku
from dataiku.customrecipe import get_recipe_config, get_output_names_for_role
from google_admin_reports import get_activities_as_dataframe
from google.oauth2.credentials import Credentials
from datetime import date

creds = Credentials(get_recipe_config()['oauth']['oauth_credentials'])
date = date.today()
try:
  date = dataiku.dku_flow_variables["DKU_DST_date"]
except:
  print('Dataset does not seem to be partionned.')
logs_df = get_activities_as_dataframe(creds, get_recipe_config()['application_name'], date)

if not logs_df.empty:
    output_A_name = get_output_names_for_role('main_output')[0]
    logs_dataset = dataiku.Dataset(output_A_name)
    logs_dataset.write_with_schema(logs_df)
