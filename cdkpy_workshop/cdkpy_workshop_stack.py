from constructs import Construct
from aws_cdk import (
    Stack,
    aws_lambda as _lambda,
    aws_apigateway as apigw,
)
from cdk_dynamo_table_view import TableViewer
from .hitcounter import HitCounter


class CdkpyWorkshopStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        my_lambda = _lambda.Function(
            self, 'HelloHandlerPython',
            runtime=_lambda.Runtime.PYTHON_3_9,
            code=_lambda.Code.from_asset('cdkpy_lambda'),
            handler='hello.handler',
        )

        hello_with_counter = HitCounter(
            self, 'PyHelloHitCounter',
            downstream=my_lambda,
        )

        apigw.LambdaRestApi(
            self, 'PythonEndpoint',
            handler=hello_with_counter.handler,
        )

        TableViewer(
            self, "PyViewHitCounter",
            title="Hello Hits",
            table=hello_with_counter.table
        )


