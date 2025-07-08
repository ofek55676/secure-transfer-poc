import boto3
from botocore.exceptions import BotoCoreError, ClientError
from logger import logger


class Secret:
    def __init__(
        self,
        table_name: str,
        region_name: str,
        aws_access_key_id: str,
        aws_secret_access_key: str,
    ):
        try:
            self.table_name = table_name
            self.dynamodb = boto3.resource(
                "dynamodb",
                aws_access_key_id=aws_access_key_id,
                aws_secret_access_key=aws_secret_access_key,
                region_name=region_name,
            )
        except Exception as e:
            raise

    def retrieve_secret(self, code_name: str) -> str:
        try:
            logger.info("Secret will retrived from DynamoDB")
            table = self.dynamodb.Table(self.table_name)
            response = table.get_item(Key={"codeName": code_name})
            item = response.get("Item")

            if item:
                return item.get("secretCode", "NOT_FOUND")
            else:
                return "NOT_FOUND"
        except (ClientError, BotoCoreError) as e:
            logger.error("Secret faileds retrived from DynamoDB")
            raise
