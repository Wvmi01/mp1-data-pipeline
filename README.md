# MP1 Data Pipeline

This pipeline loads, validates, cleans, and saves data using YAML configuration settings. It turns messy data file into a cleaned CSV file. It reads the data, checks that the needed columns exist, and removes rows with invalid numbers. It then removes duplicate rows, handles missing values, and removes unusually high or low values based on the settings in 'config/config.yaml'. It saves the cleaned file and prints a report showing how many rows and columns were removed. 'pipeline.py' runs the steps, and the supporting Python files are in the 'src/' folder. Inside 'src/', 'data_loaders.py' reads files, 'data_validator.py' checks the data, and 'data_processor.py' cleans it and creates the report. 'data_output.py' saves the result, while 'utils.py' checks file paths and sets up progress messages.

## Example command. 

```bash
python3 pipeline.py --input fixtures/sample_data.csv --output output/clean.csv --config config/config.yaml --verbose
```

## Example result

The sample starts with 100 rows. The checks remove 2 rows with invalid numbers, leaving 98. Cleaning removes another 6 rows, so the saved file ('output/clean.csv') contains 92 rows and 5 columns.

```text
{'rows_before': 98, 'rows_after': 92, 'rows_removed': 6, 'columns_before': 5, 'columns_after': 5, 'columns_removed': 0}
```
