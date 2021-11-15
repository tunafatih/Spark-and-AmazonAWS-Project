import zipfile

with zipfile.ZipFile('brazilian-ecommerce/e-commerce.zip', 'r') as zip_ref:
    zip_ref.extractall('data_for_next_job')

with zipfile.ZipFile('brazilian-ecommerce/e-commerce.zip', 'r') as zip_ref:
    zip_ref.extractall('brazilian-ecommerce')