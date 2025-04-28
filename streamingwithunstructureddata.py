from pyspark.sql import SparkSession
from config.config import configuration
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType, DateType
from udf_utils import *  # Adjusted the import path to match the project structure
import os
from pyspark.sql.functions import udf
def define_udfs():
    return{
        'extract_file_name_udf': udf(extract_file_name,StringType()),
        'extract_position_udf': udf(extract_position,StringType()),
        'extract_class_code_udf': udf(extract_class_code,StringType()),
        'extract_start_date_udf': udf(extract_start_date,DateType()),  
        'extract_end_date_udf': udf(extract_end_date,DateType()),   
        'extract_salary_udf': udf(extract_salary,StructType([
            StructField("salary_start", DoubleType(), True),
            StructField("salary_end", DoubleType(), True)
        ])),
        'extract_requirements_udf': udf(extract_requirements,StringType()),
        'extract_notes_udf': udf(extract_notes,StringType()),
        'extract_duties_udf': udf(extract_duties,StringType()),
        'extract_selection_udf': udf(extract_selection,StringType()),   
        'extract_experience_length_udf': udf(extract_experience_length,StringType()),
        'extract_job_type_udf': udf(extract_job_type,StringType()),
        'extract_education_length_udf': udf(extract_education_length,StringType()),
        'extract_school_type_udf': udf(extract_school_type,StringType()),   
        'extract_application_location_udf': udf(extract_application_location,StringType())
    }
if __name__ == "__main__":
    # Create a Spark session
    spark = (SparkSession.builder.appName("Streaming with Unstructured Data")
            .config('spark.jars.packages', 
                'org.apache.hadoop:hadoop-aws:3.3.1,'
                'com.amazonaws:aws-java-sdk:1.11.469')
            .config('spark.hadoop.fs.s3a.impl','org.apache.hadoop.fs.s3a.S3AFileSystem')
            .config('spark.hadoop.fs.s3a.access.key', configuration.get('AWS_ACCESS_KEY'))
            .config('spark.hadoop.fs.s3a.secret.key', configuration.get('AWS_SECRET_KEY'))
            .config('spark.hadoop.fs.s3a.credentials.provider', 'org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider')
            .getOrCreate())
    print("Spark session created successfully.")
#     text_input_dir=r'C:/Users/saigm/AWS-Project/input/input_text'
#     json_input_dir=r'C:/Users/saigm/AWS-Project/input/input_json'
#     csv_input_dir=r'C:/Users/saigm/AWS-Project/input/input_csv'
#     pdf_input_dir=r'C:/Users/saigm/AWS-Project/input/input_pdf'
#     img_input_dir=r'C:/Users/saigm/AWS-Project/input/input_img'
#     video_input_dir=r'C:/Users/saigm/AWS-Project/input/input_video'
#     print(f"Text input directory: {text_input_dir}")
#     data_schema = StructType([
#         StructField("file_name", StringType(), True),
#         StructField("position", IntegerType(), True),
#         StructField("classcode", StringType(), True),
#         StructField("salary_start", DoubleType(), True),
#         StructField("salary_end", DoubleType(), True),
#         StructField("start_date", DateType(), True),
#         StructField("end_date", DateType(), True),
#         StructField("req", StringType(), True),
#         StructField("notes", StringType(), True),
#         StructField("duties", StringType(), True),
#         StructField("selection", StringType(), True),
#         StructField("experience_length", StringType(), True),
#         StructField("job_type", StringType(), True),
#         StructField("education_length", StringType(), True),
#         StructField("school_type", StringType(), True),
#         StructField("application_location", StringType(), True)
#     ])
# udf=define_udfs()
# # Read streaming data from a directory
# job_bulletins_df=(spark.readStream 
#                   .format("text")
#                   .option("wholetext", "True") 
#                   .load(text_input_dir))
# job_bulletins_df.show()