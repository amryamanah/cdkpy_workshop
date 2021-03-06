import imp
from constructs import Construct
from aws_cdk import (
    Stack,
    aws_codecommit as codecommit,
)

class PyWorkshopPipelineStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Creates a CodeCommit repository called "WorkshopRepo"
        repo = codecommit.Repository(
            self, "PyWorkshopRepo",
            repository_name="PyWorkshopRepo",
        )

        # Pipeline code goes here