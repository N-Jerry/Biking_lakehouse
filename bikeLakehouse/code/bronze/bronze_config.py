BASE_PATH = '/Volumes/biking_product_sales_lakehouse/bronze/datasets/DE/'
CRM_FILES = f'{BASE_PATH}crm'
ERP_FILES = f'{BASE_PATH}erp'

files = {
    #CRM
    'customer_crm': f'{CRM_FILES}/cust_info.csv',
    'product_crm': f'{CRM_FILES}/prd_info.csv',
    'sales_crm': f'{CRM_FILES}/sales_details.csv',

    #ERP
    'customer_erp': f'{ERP_FILES}/CUST_AZ12.csv',
    'product_category_subcat_erp': f'{ERP_FILES}/PX_CAT_G1V2.csv',
    'location_erp': f'{ERP_FILES}/LOC_A101.csv'
}
