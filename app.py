import aws_cdk as cdk

from src.stack import MyStack
from src.stack_docker_lambda import StackDockerLambda
from src.stack_s3_lambda import StackS3Lambda


app = cdk.App()
MyStack(scope=app, id="MyStack")
StackS3Lambda(scope=app, id="StackS3Lambda")
StackDockerLambda(scope=app, id="StackDockerLambda")
app.synth()
