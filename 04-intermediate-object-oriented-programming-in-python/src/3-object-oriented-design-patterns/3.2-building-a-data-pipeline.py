from abc import ABC, abstractmethod

class DataPipeline:
  def _get_database(self, provider):
    if provider == "Postgres":
      return Postgres()
    elif provider == "Redshift":
      return Redshift()

  def extract_data(self, provider, query):
    database = self._get_database(provider)
    dataset = database.query_data(query)
    print(f"Extracted dataset from {provider} database")
    return dataset
  
# Create an ETL DataPipeline, query using Redshift
items_pipeline = DataPipeline()
items_pipeline.extract_data("Redshift", "SELECT * FROM items;")

# Now, switch the pipeline to Postgres
items_pipeline.extract_data("Postgres", "SELECT * FROM items;")

# Finally, create an etl_pipeline with Redshift
etl_pipeline = DataPipeline()
etl_pipeline.extract_data("Redshift", "SELECT * FROM sales;")