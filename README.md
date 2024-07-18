# Azure Data Factory Pipeline Source Extractor

This repository contains a script to extract pipeline and source details from an Azure Data Factory and save the information into an Excel file.

## Prerequisites

- Python 3.6 or higher
- Azure Subscription
- Azure Data Factory with existing pipelines
- `azure-identity`, `azure-mgmt-datafactory`, `pandas`, and `openpyxl` libraries

## Installation

1. **Clone the repository**:

    ```sh
    git clone https://github.com/nebiyu-ethio/adf-pipeline-source-extractor.git
    cd adf-pipeline-source-extractor
    ```

2. **Install the required Python packages**:

    ```sh
    pip install azure-identity azure-mgmt-datafactory pandas openpyxl
    ```

## Configuration

1. Open the `adf_pipeline_source_extractor.py` file in a text editor.

2. Replace the placeholder values with your actual Azure subscription ID, resource group name, and data factory name:

    ```python
    # Set up your credentials and client
    subscription_id = 'your-subscription-id'
    resource_group_name = 'your-resource-group-name'
    factory_name = 'your-data-factory-name'
    ```

## Usage

1. Ensure you have the required Azure credentials set up. The script uses the `DefaultAzureCredential` from the `azure-identity` library, which supports various authentication methods. Make sure you have the appropriate environment variables or Azure CLI logged in.

2. Run the script:

    ```sh
    python adf_pipeline_source_extractor.py
    ```

3. After the script executes successfully, it will generate an `output.xlsx` file in the same directory. This file will contain two columns: `Pipeline` and `Source`.

## Script Details

The script does the following:

1. Sets up credentials and initializes the Azure Data Factory Management client.
2. Lists all pipelines in the specified data factory.
3. Iterates through each pipeline to extract details of the `Copy` activities and their sources.
4. Collects the pipeline names and source names into a list.
5. Converts the list to a pandas DataFrame and writes it to an Excel file named `output.xlsx`.

## Example Output

The `output.xlsx` file will have the following structure:

| Pipeline       | Source        |
|----------------|---------------|
| pipeline_name1 | source_name1  |
| pipeline_name2 | source_name2  |
| ...            | ...           |