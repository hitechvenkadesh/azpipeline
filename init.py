import logging
import azure.functions as func

from azure.devops.connection import connection
from msrest.authentication import BasicAuthentication
from .creds import PERSONAL_ACCESS_TOKEN,ORGANIZATION_URL,PROJECT_NAME

def create_pipeline_client():
  creadentials = BasicAuthentication("",PERSONAL_ACCESS_TOKEN)
  connection = Connection(base_url=ORGANIZATION_URL,creds=credeentials)
  pipeline_client = connection.clients_v5_1.get_pipeline_client()
  return pipeline_client

def build_pipeline(pipe_id,run_params,pipe_version=None):
    pipeline_client = create_pipeline_client()
    logging.info(run_params)
    logging.info("Running Pipeline with id"+ str(pipe_id))
    #try:
    pipeline_client.run_pipeline(
        run_parameters=run_params,
        project=PROJECT_NAME,
        pipeline_id=pipe_id,
        pipeline_version=pipe_version)
    logging.info("Pipeline run succesfullyactivated.")

def main(myblob: func.InputStream):
    logging.info(f"python blob trigger function processed blob\n"
                 f"Name:{myblob.name}\n"
                 f"Blob Size:{myblob.length}bytes")


    logging.info("Automation script to run piplines on Devops.")
    run_params={'branch/tag':"master"}
    build_pipeline("2",run_params,None)
    
        
