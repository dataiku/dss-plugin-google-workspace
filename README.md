# Google Workspace Plugin

This plugin is a crawler for Google Workspace logs.
It provides a recipe that retrieves the logs from the Google API using OAuth 2.0, and stores them into a daily-partitioned dataset.

## Setup instructions
1. Create a Google Cloud Platform project and enable the **Reports API**. ([How to create a project](https://developers.google.com/workspace/guides/create-project), [How to enable APIs](https://developers.google.com/workspace/guides/enable-apis))
2. Create OAuth 2.0 credentials for a **Desktop app** in your Google Cloud Console and write down the **Client ID** and the **Client secret**. ([How to create credentials](https://developers.google.com/workspace/guides/create-credentials#desktop-app))
3. Install the current plugin on your Dataiku DSS instance.
4. In DSS, go to the plugin settings, click on **OAuth 2.0**, then create a new preset and give it a name. (The preset name will be shown in the recipe settings and in the user profile settings.)
5. Configure the preset with the **Client ID** and the **Client secret** obtained at step 2.
6. Go to your user profile and open the Credentials tab. Click on the edit icon of the preset. Follow the procedure to configure your personal Google credentials.

## Usage instructions
1. Create a new **Google Workspace logs crawler** recipe.
2. Configure the output of the recipe with a daily-partitioned dataset.
3. In the recipe settings:
	- select the preset attached to your credentials (see steps 4 to 6 from the [Setup instructions](#-Setup-instructions) above)
	- select the application name for which you want to retrieve the event logs. (See the [Google documentation](https://developers.google.com/admin-sdk/reports/reference/rest/v1/activities/list#ApplicationName) for more details on each option.)

## Changelog
See [CHANGELOG.md](./CHANGELOG.md)

## Licence

Copyright 2022 Dataiku SAS

This plugin is distributed under the Apache License version 2.0
