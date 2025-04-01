# CST8919 - Lab 4 - Azure Key Vault Exploration
Donna Ha - 041174159

## Prerequisites
- Python
- Azure CLI
- Azure Account (Key Vault)

This program assumes you already have a Key Vault created with correct access permissions given to your Azure account.

## Information on code
This code template is based on Microsoft Learn's quick start article: <br/> ["Quickstart: Azure Key Vault secret client library for Python"](https://learn.microsoft.com/en-us/azure/key-vault/secrets/quick-create-python?tabs=azure-cli).


### Environment Variable
The code uses an environment variable that is set using the following command:

Linux
```
export KEY_VAULT_NAME=<your-unique-keyvault-name>
```
    
Command Prompt
```
set KEY_VAULT_NAME=<your-unique-keyvault-name>
```

### To Run This Simple Application
1. Clone/Download this repository
2. Set your environment variable for the KEY_VAULT_NAME
3. Log in to Azure CLI
4. Change into this directory, and run 
    ```
    python add-secret.py 
    ```

### Authentication
The article shows us how to authenticate using DefaultAzureCredential, which would potentially need more environment variables for AZURE_CLIENT_ID, AZURE_TENANT_ID, AZURE_CLIENT_SECRET. 

As I am already logged in and using Azure CLI, I switched the authentication method from DefaultAzureCredential to AzureCliCredential. AzureCliCredential uses the authentication provided by Azure CLI, which is simpler and easier in my case as I don't need to do anything further.

### Deletion
I have commented out the code that deletes the secret afterwards. However if you would like to delete the secret right after creation, you can uncomment the code, or delete it straight from the Azure Portal.


