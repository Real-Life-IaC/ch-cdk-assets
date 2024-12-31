import aws_cdk as cdk

from aws_cdk import aws_lambda as _lambda
from constructs import Construct


class StackS3Lambda(cdk.Stack):
    """Create a Stack"""

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create a Lambda function from s3 files
        _lambda.Function(
            scope=self,
            id="LambdaFunction",
            runtime=_lambda.Runtime.PYTHON_3_11,
            handler="handler.lambda_handler",
            code=_lambda.Code.from_asset(
                path="assets/lambda_s3/",
            ),
        )
