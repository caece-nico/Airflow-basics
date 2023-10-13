from airflow.models.base_operator import BaseOPerator
from airflow.hooks.s3_hook import S3Hook

class CustomS3toS3(BaseOPerator):
    def __init__(
                    self, s3_conn_ori: str, s3_key_ori: str, s3_bucket_ori: str, s3_conn_dest: str, 
                    s3_key_dest: str, s3_bucket_dest: str, file_name: str, s3_aws_hook_ori: str, 
                    s3_aws_hook_dest:str,  **kwargs ):
    super().__init__(**kwargs)
    self.s3_conn_ori = s3_conn_ori
    self.s3_key_ori = s3_key_ori
    self.s3_bucket_ori = s3_bucket_ori
    self.s3_conn_dest = s3_conn_dest
    self.s3_key_dest = s3_key_dest
    self.s3_bucket_dest = s3_bucket_dest
    self.file_name = file_name
    self.s3_aws_hook_ori = S3Hook(s3_conn_ori)
    self.s3_aws_hook_dest = S3Hook(s3_bucket_dest)

    def execute(self, context):
        self.s3_aws_hook_ori.get_key(filename=self.file_name)
        self.s3

