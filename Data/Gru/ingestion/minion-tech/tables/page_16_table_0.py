
import pandas as pd

data = {
    'Description': [
        'Net Income', 'Depreciation', 'Changes in Working Capital', 'Net Cash from Operating Activities',
        'Capital Expenditures', 'Net Cash from Investing Activities',
        'Long-term Debt Financing', 'Net Cash from Financing Activities',
        'Net Increase in Cash', 'Cash at Beginning of Period', 'Cash at End of Period'
    ],
    'Amount (USD)': [
        84000, 50000, -100000, 34000,
        -200000, -200000,
        1700000, 1700000,
        1534000, -1034000, 500000
    ]
}

df_cash_flow_statement_123456 = pd.DataFrame(data)
