
# Summary of the TEXT EXTRACT:
# Offsetting of Derivatives (1)
# 
# The Corporation's ALM and risk management activities include the use of derivatives to mitigate risk to the Corporation including derivatives designated in qualifying hedge accounting relationships and derivatives used in other risk management activities. Interest rate, foreign exchange, equity, commodity and credit contracts are utilized in the Corporation's ALM and risk management activities.
# 
# The Corporation maintains an overall interest rate risk management strategy that incorporates the use of interest rate contracts, which are generally non-leveraged generic interest rate and basis swaps, options, futures and forwards, to minimize significant fluctuations in earnings caused by interest rate volatility. The Corporation's goal is to manage interest rate sensitivity and volatility so that movements in interest rates do not significantly adversely affect earnings or capital. As a result of interest rate fluctuations, hedged fixed-rate assets and liabilities appreciate or depreciate in fair value. Gains or losses on the derivative instruments that are linked to the hedged fixed-rate assets and liabilities are expected to substantially offset this unrealized appreciation or depreciation.
# 
# Market risk, including interest rate risk, can be substantial in the mortgage business. Market risk in the mortgage business is the risk that values of mortgage assets or revenues will be adversely affected by changes in market conditions such as interest rate movements. To mitigate the interest rate risk in mortgage banking production income, the Corporation utilizes forward loan sale commitments and other derivative instruments, including purchased options, and certain debt securities. The Corporation also utilizes derivatives such as interest rate options, interest rate swaps, forward settlement contracts and eurodollar futures to hedge certain market risks of MSRs. For more information on MSRs, see Note 20 - Fair Value Measurements.
# 
# The Corporation uses foreign exchange contracts to manage the foreign exchange risk associated with certain foreign currency-denominated assets and liabilities, as well as the Corporation's investments in non-U.S. subsidiaries. Foreign exchange contracts, which include spot and forward contracts, represent agreements to exchange the currency of one country for the currency of another country at an agreed-upon price on an agreed-upon settlement date. Exposure to loss on these contracts will increase or decrease over their respective lives as currency exchange and interest rates fluctuate.
# 
# The Corporation purchases credit derivatives to manage credit risk related to certain funded and unfunded credit exposures. Credit derivatives include CDS, total return swaps and swaptions. These derivatives are recorded on the Consolidated Balance Sheet at fair value with changes in fair value recorded in other income.
# 
# Derivatives Designated as Accounting Hedges
# 
# The Corporation uses various types of interest rate and foreign exchange derivative contracts to protect against changes in the fair value of its assets and liabilities due to fluctuations in interest rates and exchange rates (fair value hedges). The Corporation also uses these types of contracts to protect against changes in the cash flows of its assets and liabilities, and other forecasted transactions (cash flow hedges). The Corporation hedges its net investment in consolidated non-U.S. operations determined to have functional currencies other than the U.S. dollar using forward

# START OF CODE BLOCK af497312

# Variables:
# var_derivative_assets_Dollars_in_billions_1: Derivative Assets (Dollars in billions) on December 31, 2018
# var_derivative_liabilities_Dollars_in_billions_1: Derivative Liabilities (Dollars in billions) on December 31, 2018
# var_derivative_assets_Dollars_in_billions_2: Derivative Assets (Dollars in billions) on December 31, 2017
# var_derivative_liabilities_Dollars_in_billions_2: Derivative Liabilities (Dollars in billions) on December 31, 2017
# var_interest_rate_contracts_OTC_1: Interest rate contracts - Over-the-counter on December 31, 2018
# var_interest_rate_contracts_OTC_2: Interest rate contracts - Over-the-counter on December 31, 2017
# var_interest_rate_contracts_OTC_cleared_1: Interest rate contracts - Over-the-counter cleared on December 31, 2018
# var_interest_rate_contracts_OTC_cleared_2: Interest rate contracts - Over-the-counter cleared on December 31, 2017
# var_foreign_exchange_contracts_OTC_1: Foreign exchange contracts - Over-the-counter on December 31, 2018
# var_foreign_exchange_contracts_OTC_2: Foreign exchange contracts - Over-the-counter on December 31, 2017
# var_foreign_exchange_contracts_OTC_cleared_1: Foreign exchange contracts - Over-the-counter cleared on December 31, 2018
# var_foreign_exchange_contracts_OTC_cleared_2: Foreign exchange contracts - Over-the-counter cleared on December 31, 2017
# var_equity_contracts_OTC_1: Equity contracts - Over-the-counter on December 31, 2018
# var_equity_contracts_OTC_2: Equity contracts - Over-the-counter on December 31, 2017
# var_equity_contracts_exchange_traded_1: Equity contracts - Exchange-traded on December 31, 2018
# var_equity_contracts_exchange_traded_2: Equity contracts - Exchange-traded on December 31, 2017
# var_commodity_contracts_OTC_1: Commodity contracts - Over-the-counter on December 31, 2018
# var_commodity_contracts_OTC_2: Commodity contracts - Over-the-counter on December 31, 2017
# var_commodity_contracts_exchange_traded_1: Commodity contracts - Exchange-traded on December 31, 2018
# var_commodity_contracts_exchange_traded_2: Commodity contracts - Exchange-traded on December 31, 2017
# var_credit_derivatives_OTC_1: Credit derivatives - Over-the-counter on December 31, 2018
# var_credit_derivatives_OTC_2: Credit derivatives - Over-the-counter on December 31, 2017
# var_credit_derivatives_OTC_cleared_1: Credit derivatives - Over-the-counter cleared on December 31, 2018
# var_credit_derivatives_OTC_cleared_2: Credit derivatives - Over-the-counter cleared on December 31, 2017
# var_total_gross_derivative_assets_liabilities_before_netting_OTC_1: Total gross derivative assets/liabilities, before netting - Over-the-counter on December 31, 2018
# var_total_gross_derivative_assets_liabilities_before_netting_OTC_2: Total gross derivative assets/liabilities, before netting - Over-the-counter on December 31, 2017
# var_total_gross_derivative_assets_liabilities_before_netting_exchange_traded_1: Total gross derivative assets/liabilities, before netting - Exchange-traded on December 31, 2018
# var_total_gross_derivative_assets_liabilities_before_netting_exchange_traded_2: Total gross derivative assets/liabilities, before netting - Exchange-traded on December 31, 2017
# var_total_gross_derivative_assets_liabilities_before_netting_OTC_cleared_1: Total gross derivative assets/liabilities, before netting - Over-the-counter cleared on December 31, 2018
# var_total_gross_derivative_assets_liabilities_before_netting_OTC_cleared_2: Total gross derivative assets/liabilities, before netting - Over-the-counter cleared on December 31, 2017
# var_derivative_assets_liabilities_after_netting_1: Derivative assets/liabilities, after netting on December 31, 2018
# var_derivative_assets_liabilities_after_netting_2: Derivative assets/liabilities, after netting on December 31, 2017
# var_other_gross_derivative_assets_liabilities_1: Other gross derivative assets/liabilities on December 31, 2018
# var_other_gross_derivative_assets_liabilities_2: Other gross derivative assets/liabilities on December 31, 2017
# var_total_derivative_assets_liabilities_1: Total derivative assets/liabilities on December 31, 2018
# var_total_derivative_assets_liabilities_2: Total derivative assets/liabilities on December 31, 2017
# var_total_net_derivative_assets_liabilities_1: Total net derivative assets/liabilities on December 31, 2018
# var_total_net_derivative_assets_liabilities_2: Total net derivative assets/liabilities on December 31, 2017

var_derivative_assets_Dollars_in_billions_1 = 43.7
var_derivative_liabilities_Dollars_in_billions_1 = 37.9
var_derivative_assets_Dollars_in_billions_2 = 37.8
var_derivative_liabilities_Dollars_in_billions_2 = 34.3
var_interest_rate_contracts_OTC_1 = 174.2
var_interest_rate_contracts_OTC_2 = 211.7
var_interest_rate_contracts_OTC_cleared_1 = 4.8
var_interest_rate_contracts_OTC_cleared_2 = 1.9
var_foreign_exchange_contracts_OTC_1 = 82.5
var_foreign_exchange_contracts_OTC_2 = 78.7
var_foreign_exchange_contracts_OTC_cleared_1 = 0.9
var_foreign_exchange_contracts_OTC_cleared_2 = 0.9
var_equity_contracts_OTC_1 = 24.6
var_equity_contracts_OTC_2 = 18.3
var_equity_contracts_exchange_traded_1 = 16.1
var_equity_contracts_exchange_traded_2 = 9.1
var_commodity_contracts_OTC_1 = 3.5
var_commodity_contracts_OTC_2 = 2.9
var_commodity_contracts_exchange_traded_1 = 1.0
var_commodity_contracts_exchange_traded_2 = 0.7
var_credit_derivatives_OTC_1 = 7.7
var_credit_derivatives_OTC_2 = 9.1
var_credit_derivatives_OTC_cleared_1 = 2.5
var_credit_derivatives_OTC_cleared_2 = 6.1
var_total_gross_derivative_assets_liabilities_before_netting_OTC_1 = 292.5
var_total_gross_derivative_assets_liabilities_before_netting_OTC_2 = 320.7
var_total_gross_derivative_assets_liabilities_before_netting_exchange_traded_1 = 17.1
var_total_gross_derivative_assets_liabilities_before_netting_exchange_traded_2 = 9.8
var_total_gross_derivative_assets_liabilities_before_netting_OTC_cleared_1 = 8.2
var_total_gross_derivative_assets_liabilities_before_netting_OTC_cleared_2 = 8.9
var_derivative_assets_liabilities_after_netting_1 = 32.7
var_derivative_assets_liabilities_after_netting_2 = 25.6
var_other_gross_derivative_assets_liabilities_1 = 11.0
var_other_gross_derivative_assets_liabilities_2 = 12.2
var_total_derivative_assets_liabilities_1 = 43.7
var_total_derivative_assets_liabilities_2 = 37.8
var_total_net_derivative_assets_liabilities_1 = 27.4
var_total_net_derivative_assets_liabilities_2 = 26.6

# END OF CODE BLOCK af497312
