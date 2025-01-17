
# Summary of the TEXT EXTRACT:
# Table 25 presents outstandings, nonperforming loans and net charge-offs by certain state concentrations for the residential mortgage portfolio.
# The Los Angeles-Long Beach-Santa Ana Metropolitan Statistical Area (MSA) within California represented 16 percent of outstandings at both December 31, 2018 and 2017.
# In the New York area, the New York-Northern New Jersey-Long Island MSA made up 13 percent of outstandings at both December 31, 2018 and 2017.
# Table 25 Residential Mortgage State Concentrations
# California: Outstandings (1) = $74,463 million, Nonperforming (1) = $314 million, Net Charge-offs (2) = $22 million
# New York (3): Outstandings (1) = $19,085 million, Nonperforming (1) = $222 million, Net Charge-offs (2) = $10 million
# Florida (3): Outstandings (1) = $11,296 million, Nonperforming (1) = $221 million, Net Charge-offs (2) = $6 million
# Texas: Outstandings (1) = $7,747 million, Nonperforming (1) = $102 million, Net Charge-offs (2) = $4 million
# New Jersey (3): Outstandings (1) = $6,959 million, Nonperforming (1) = $98 million, Net Charge-offs (2) = $8 million
# Other: Outstandings (1) = $65,077 million, Nonperforming (1) = $936 million, Net Charge-offs (2) = $34 million
# Residential mortgage loans (4) = $184,627 million, Nonperforming (1) = $1,893 million, Net Charge-offs (2) = $28 million
# Fully-insured loan portfolio = $20,130 million
# Purchased credit-impaired residential mortgage loan portfolio (5) = $3,800 million
# Total residential mortgage loan portfolio = $208,557 million

# Home Equity
# Home equity portfolio = 11 percent of the consumer portfolio
# HELOC portfolio: Outstanding balance = $44.3 billion, 92 percent of the total home equity portfolio
# Home equity loan portfolio: Outstanding balance = $1.8 billion, 4 percent of the total home equity portfolio
# Reverse mortgage portfolio: Outstanding balance = $2.2 billion, 4 percent of the total home equity portfolio
# 75 percent of the home equity portfolio was in Consumer Banking, 17 percent was in All Other, and the remainder was primarily in GWIM
# Outstanding balances in the home equity portfolio decreased $9.5 billion in 2018 primarily due to paydowns and loan sales of $2.7 billion outpacing new originations and draws on existing lines
# Of the total home equity portfolio at December 31, 2018 and 2017, $17.3 billion and $18.7 billion, or 36 percent and 32 percent, were in first-lien positions
# Outstanding balances in the home equity portfolio that were in a second-lien or more junior-lien position and where we also held the first-lien loan totaled $7.9 billion, or 17 percent of our total home equity portfolio excluding the PCI loan portfolio
# Unused HELOCs totaled $43.1 billion and $44.2 billion at December 31, 2018 and 2017
# The HELOC utilization rate was 51 percent and 54 percent at December 31, 2018 and 2017

# START OF CODE BLOCK 62998754

# Variables:
# var_outstandings_California_62998754: Represents the outstandings in California for the residential mortgage portfolio
# var_nonperforming_California_62998754: Represents the nonperforming loans in California for the residential mortgage portfolio
# var_net_chargeoffs_California_62998754: Represents the net charge-offs in California for the residential mortgage portfolio
# var_outstandings_New_York_62998754: Represents the outstandings in New York for the residential mortgage portfolio
# var_nonperforming_New_York_62998754: Represents the nonperforming loans in New York for the residential mortgage portfolio
# var_net_chargeoffs_New_York_62998754: Represents the net charge-offs in New York for the residential mortgage portfolio
# var_outstandings_Florida_62998754: Represents the outstandings in Florida for the residential mortgage portfolio
# var_nonperforming_Florida_62998754: Represents the nonperforming loans in Florida for the residential mortgage portfolio
# var_net_chargeoffs_Florida_62998754: Represents the net charge-offs in Florida for the residential mortgage portfolio
# var_outstandings_Texas_62998754: Represents the outstandings in Texas for the residential mortgage portfolio
# var_nonperforming_Texas_62998754: Represents the nonperforming loans in Texas for the residential mortgage portfolio
# var_net_chargeoffs_Texas_62998754: Represents the net charge-offs in Texas for the residential mortgage portfolio
# var_outstandings_New_Jersey_62998754: Represents the outstandings in New Jersey for the residential mortgage portfolio
# var_nonperforming_New_Jersey_62998754: Represents the nonperforming loans in New Jersey for the residential mortgage portfolio
# var_net_chargeoffs_New_Jersey_62998754: Represents the net charge-offs in New Jersey for the residential mortgage portfolio
# var_outstandings_Other_62998754: Represents the outstandings in Other states for the residential mortgage portfolio
# var_nonperforming_Other_62998754: Represents the nonperforming loans in Other states for the residential mortgage portfolio
# var_net_chargeoffs_Other_62998754: Represents the net charge-offs in Other states for the residential mortgage portfolio
# var_outstandings_Residential_mortgage_loans_62998754: Represents the outstandings for the residential mortgage loans
# var_nonperforming_Residential_mortgage_loans_62998754: Represents the nonperforming loans for the residential mortgage loans
# var_net_chargeoffs_Residential_mortgage_loans_62998754: Represents the net charge-offs for the residential mortgage loans
# var_fully_insured_loan_portfolio_62998754: Represents the outstanding balance for the fully-insured loan portfolio
# var_purchased_credit_impaired_residential_mortgage_loan_portfolio_62998754: Represents the outstanding balance for the purchased credit-impaired residential mortgage loan portfolio
# var_total_residential_mortgage_loan_portfolio_62998754: Represents the total outstanding balance for the residential mortgage loan portfolio
# var_home_equity_portfolio_62998754: Represents the percentage of the home equity portfolio in the consumer portfolio
# var_outstanding_balance_HELOC_62998754: Represents the outstanding balance for the HELOC portfolio
# var_outstanding_balance_home_equity_loan_62998754: Represents the outstanding balance for the home equity loan portfolio
# var_outstanding_balance_reverse_mortgage_62998754: Represents the outstanding balance for the reverse mortgage portfolio
# var_home_equity_portfolio_Consumer_Banking_62998754: Represents the percentage of the home equity portfolio in Consumer Banking
# var_home_equity_portfolio_All_Other_62998754: Represents the percentage of the home equity portfolio in All Other
# var_home_equity_portfolio_GWIM_62998754: Represents the percentage of the home equity portfolio in GWIM
# var_outstanding_balance_change_2018_62998754: Represents the change in outstanding balances in the home equity portfolio in 2018
# var_outstanding_balance_first_lien_62998754: Represents the outstanding balances in the home equity portfolio in first-lien positions
# var_outstanding_balance_second_lien_62998754: Represents the outstanding balances in the home equity portfolio in second-lien or more junior-lien positions
# var_unused_HELOCs_62998754: Represents the total unused HELOCs
# var_HELOC_utilization_rate_62998754: Represents the HELOC utilization rate

var_outstandings_California_62998754 = 74463
var_nonperforming_California_62998754 = 314
var_net_chargeoffs_California_62998754 = -22

var_outstandings_New_York_62998754 = 19085
var_nonperforming_New_York_62998754 = 222
var_net_chargeoffs_New_York_62998754 = 10

var_outstandings_Florida_62998754 = 11296
var_nonperforming_Florida_62998754 = 221
var_net_chargeoffs_Florida_62998754 = -6

var_outstandings_Texas_62998754 = 7747
var_nonperforming_Texas_62998754 = 102
var_net_chargeoffs_Texas_62998754 = 4

var_outstandings_New_Jersey_62998754 = 6959
var_nonperforming_New_Jersey_62998754 = 98
var_net_chargeoffs_New_Jersey_62998754 = 8

var_outstandings_Other_62998754 = 65077
var_nonperforming_Other_62998754 = 936
var_net_chargeoffs_Other_62998754 = 34

var_outstandings_Residential_mortgage_loans_62998754 = 184627
var_nonperforming_Residential_mortgage_loans_62998754 = 1893
var_net_chargeoffs_Residential_mortgage_loans_62998754 = 28

var_fully_insured_loan_portfolio_62998754 = 20130
var_purchased_credit_impaired_residential_mortgage_loan_portfolio_62998754 = 3800
var_total_residential_mortgage_loan_portfolio_62998754 = 208557

var_home_equity_portfolio_62998754 = 11

var_outstanding_balance_HELOC_62998754 = 44300
var_outstanding_balance_home_equity_loan_62998754 = 1800
var_outstanding_balance_reverse_mortgage_62998754 = 2200

var_home_equity_portfolio_Consumer_Banking_62998754 = 75
var_home_equity_portfolio_All_Other_62998754 = 17
var_home_equity_portfolio_GWIM_62998754 = 8

var_outstanding_balance_change_2018_62998754 = -9500

var_outstanding_balance_first_lien_62998754 = 17300
var_outstanding_balance_second_lien_62998754 = 7900

var_unused_HELOCs_62998754 = 43100

var_HELOC_utilization_rate_62998754 = 51

# Markdown table of numerical data:
| Variable Name | Value |
| --- | --- |
| var_outstandings_California_62998754 | 74463 |
| var_nonperforming_California_62998754 | 314 |
| var_net_chargeoffs_California_62998754 | -22 |
| var_outstandings_New_York_62998754 | 19085 |
| var_nonperforming_New_York_62998754 | 222 |
| var_net_chargeoffs_New_York_62998754 | 10 |
| var_outstandings_Florida_62998754 | 11296 |
| var_nonperforming_Florida_62998754 | 221 |
| var_net_chargeoffs_Florida_62998754 | -6 |
| var_outstandings_Texas_62998754 | 7747 |
| var_nonperforming_Texas_62998754 | 102 |
| var_net_chargeoffs_Texas_62998754 | 4 |
| var_outstandings_New_Jersey_62998754 | 6959 |
| var_nonperforming_New_Jersey_62998754 | 98 |
| var_net_chargeoffs_New_Jersey_62998754 | 8 |
| var_outstandings_Other_62998754 | 65077 |
| var_nonperforming_Other_62998754 | 936 |
| var_net_chargeoffs_Other_62998754 | 34 |
| var_outstandings_Residential_mortgage_loans_62998754 | 184627 |
| var_nonperforming_Residential_mortgage_loans_62998754 | 1893 |
| var_net_chargeoffs_Residential_mortgage_loans_62998754 | 28 |
| var_fully_insured_loan_portfolio_62998754 | 20130 |
| var_purchased_credit_impaired_residential_mortgage_loan_portfolio_62998754 | 3800 |
| var_total_residential_mortgage_loan_portfolio_62998754 | 208557 |
| var_home_equity_portfolio_62998754 | 11 |
| var_outstanding_balance_HELOC_62998754 | 44300 |
| var_outstanding_balance_home_equity_loan_62998754 | 1800 |
| var_outstanding_balance_reverse_mortgage_62998754 | 2200 |
| var_home_equity_portfolio_Consumer_Banking_62998754 | 75 |
| var_home_equity_portfolio_All_Other_62998754 | 17 |
| var_home_equity_portfolio_GWIM_62998754 | 8 |
| var_outstanding_balance_change_2018_62998754 | -9500 |
| var_outstanding_balance_first_lien_62998754 | 17300 |
| var_outstanding_balance_second_lien_62998754 | 7900 |
| var_unused_HELOCs_62998754 | 43100 |
| var_HELOC_utilization_rate_62998754 | 51 |

# END OF CODE BLOCK 62998754
