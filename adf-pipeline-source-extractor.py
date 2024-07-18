import pandas as pd
from azure.identity import DefaultAzureCredential
from azure.mgmt.datafactory import DataFactoryManagementClient

# Set up your credentials and client
subscription_id = 'your-subscription-id'
resource_group_name = 'your-resource-group-name'
factory_name = 'your-data-factory-name'

credential = DefaultAzureCredential()
adf_client = DataFactoryManagementClient(credential, subscription_id)

# List all pipelines in the data factory
pipelines = adf_client.pipelines.list_by_factory(resource_group_name, factory_name)

# Prepare a list to hold the data
data = []

# Loop through each pipeline and get the source details
for pipeline in pipelines:
    pipeline_name = pipeline.name
    pipeline_details = adf_client.pipelines.get(resource_group_name, factory_name, pipeline_name)
    
    for activity in pipeline_details.activities:
        if activity.type == 'Copy' and activity.inputs:
            for input_item in activity.inputs:
                source = input_item.reference_name
                if source:
                    data.append([pipeline_name, source])

# Create a DataFrame and save to Excel
df = pd.DataFrame(data, columns=['Pipeline', 'Source'])
df.to_excel('output.xlsx', index=False)