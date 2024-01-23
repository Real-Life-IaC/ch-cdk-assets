import aws_cdk as cdk

from aws_cdk import aws_lambda as lambda_
from constructs import Construct


class StackDockerLambda(cdk.Stack):
    """Create a Stack"""

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create a Lambda function from Docker image
        lambda_.DockerImageFunction(
            scope=self,
            id="MyFunction",
            code=lambda_.DockerImageCode.from_image_asset(
                directory="assets/lambda_docker/",
            ),
        )
