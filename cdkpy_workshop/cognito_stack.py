from constructs import Construct
from aws_cdk import (
    Stack,
    aws_cognito as cognito,
    aws_iam as iam,
)

class CognitoStack(Stack):
    
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        identity_pool = cognito.UserPool(
            self, "cdkpy-user-pool",
            user_pool_name="cdkpy-workshop-user-pool",
            allow_unauthenticated_identities=True,
        )
