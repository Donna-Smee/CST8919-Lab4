import os
from azure.keyvault.secrets import SecretClient
from azure.identity import AzureCliCredential

keyVaultName = os.environ["KEY_VAULT_NAME"]

KVUri = f"https://{keyVaultName}.vault.azure.net"

credential = AzureCliCredential()
client = SecretClient(vault_url=KVUri, credential=credential)


secretName = input("Enter a name for your secret: ")
secretValue = input("Enter a value for your secret: ")

print(f"Creating a secret in {keyVaultName} called '{secretName}' with the value '{secretValue}' ...")

client.set_secret(secretName, secretValue)

print("Your secret has been created.")

print(f"Retrieving your secret from {keyVaultName}.")

retrieved_secret = client.get_secret(secretName)

print(f"Your secret name is '{retrieved_secret.name}'.")
print(f"Your secret value is '{retrieved_secret.value}'.")


# Deleting secret
'''
print(f"Deleting your secret from {keyVaultName} ...")

poller = client.begin_delete_secret("secret1-ha000070")
deleted_secret = poller.result()

print(" done.")'
'''