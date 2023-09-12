
from pyspark.sql import SparkSession

class SparkSS :
    def __init__(self, appl_name) :
        self.appl_name = appl_name
    
    def getSpark(self) : 
         self._spark = (SparkSession.builder.appName(self.appl_name)
                .config("spark.driver.host","127.0.0.1") 
                .config("spark.driver.bindAddress","127.0.0.1")
                .getOrCreate())
         
         return self._spark
