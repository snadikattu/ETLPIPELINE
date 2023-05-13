# a robust simple ETLPIPELINE
Above ETL pipeline script can test any of Config.ini please add include error handling, logging, testing and often, multiple data sources and destinations. 

Add GitLab CI/CD Configuration**:`.etl-ci.yml` 
For Reference  
In this configuration, we're defining the variables that our ETL script expects: `DATABASE_URI`, `TABLE_NAME`, and `DATA_FILENAME`. We're also installing the `sqlalchemy` package, which our script uses to load data into a SQL database.

Now , **Run the ETL Job**:

After pushing your changes, GitLab will automatically detect the `.gitlab-ci.yml` file and start a new pipeline with a single stage: `etl`. You can view the progress of this pipeline in the GitLab dashboard as stages 

**Retrieve the Logs**:

Once the pipeline has completed, you can download the `etl.log`  file from the GitLab dashboard to check for any errors or issues that occurred during the ETL process.
