import aws_cdk as cdk

from aws_cdk import aws_ecr_assets as ecr_assets
from aws_cdk import aws_iam as iam
from aws_cdk import aws_s3_assets as s3_assets
from constructs import Construct


class MyStack(cdk.Stack):
    """Create a Stack"""

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create an asset from a local file
        s3_assets.Asset(
            scope=self,
            id="FileAsset",
            path="assets/s3_assets.png",
        )

        # Create an asset from a directory
        # excluding files with a .md extension
        s3_asset = s3_assets.Asset(
            scope=self,
            id="DirectoryAsset",
            path="assets/static_site/",
            exclude=["*.md"],
        )

        # Accessing some of the asset attributes
        # and printing them to the console
        cdk.CfnOutput(
            scope=self,
            id="AssetBucketName",
            value=s3_asset.s3_bucket_name,
        )
        cdk.CfnOutput(
            scope=self,
            id="AssetKey",
            value=s3_asset.s3_object_key,
        )
        cdk.CfnOutput(
            scope=self,
            id="AssetIsZipArchive",
            value=str(
                s3_asset.is_zip_archive,
            ),
        )

        # Granting read permissions to a role
        role = iam.Role(
            scope=self,
            id="Role",
            assumed_by=iam.ServicePrincipal("ec2.amazonaws.com"),
        )
        s3_asset.grant_read(role)

        # Create an asset from a Docker image
        ecr_asset = ecr_assets.DockerImageAsset(
            scope=self,
            id="EcrAsset",
            directory="assets/lambda_docker",
        )

        cdk.CfnOutput(
            scope=self,
            id="AssetImageUri",
            value=ecr_asset.image_uri,
        )
