import boto3

client = session.client('marketplace-entitlement', verify=False)
entitlements = client.get_entitlements(ProductCode='63sbazrz7hre7ensv0gmssh98')
pp.pprint(entitlements)
