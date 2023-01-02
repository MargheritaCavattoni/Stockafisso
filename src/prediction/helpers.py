def retrieve_company_code(df, company_name):
     df_company = df[df['COMPANY NAME'].str.contains(company_name, na=False)]
     return df_company
