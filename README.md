# Duka Sales Analysis and Agent Transaction Data Cleaning

## Project Overview

This project demonstrates practical data analytics skills through two engagements:

1. **Duka Sales Analysis:** Exploring sales data to identify branch performance, product revenue trends, sales channels, and monthly performance.
2. **Agent Transaction Data Cleaning:** Identifying and correcting data quality issues in agent transaction records while maintaining an audit log.

The project uses Python, Pandas, NumPy, Jupyter Notebook, Excel, and OpenPyXL.

## Project Objectives

- Inspect and understand raw datasets.
- Clean, transform, and validate data.
- Perform exploratory data analysis.
- Engineer useful analytical features.
- Generate business insights and summaries.
- Export cleaned datasets and Excel reports.
- Document data quality improvements and privacy considerations.

## Project Structure

```text
plp-da-a3-duka-sales-and-agent-cleanup/
│
├── excel/
│   └── duka_branch_summary.xlsx
│
├── outputs/
│   ├── premium_online_coast_capital.csv
│   └── agent_transactions_clean.csv
│
├── generate_data.py
├── cleaning_pipeline.py
├── duka_sales_exploration.ipynb
├── agent_cleanup.ipynb
├── requirements.txt
└── README.md
```

## Engagement 1: Duka Sales Analysis

### Dataset Overview

The Duka sales dataset contains 1,000 sales records with seven original columns:

- order_id
- order_date
- branch
- product
- quantity
- channel
- unit_price

The analysis covers five branches: Nairobi, Mombasa, Kisumu, Nakuru, and Eldoret.

### Data Preparation and Feature Engineering

The analysis included:

- Dataset inspection and validation.
- Date conversion and standardization.
- Revenue calculation.
- Month and weekday extraction.
- Weekend identification.
- Price band classification.
- Branch, product, channel, and monthly aggregations.

### Key Findings

1. The dataset contains **1,000 sales records** across five branches, with no missing values in the original columns.
2. Nairobi recorded the highest branch revenue of **KES 26,106,100** from 376 orders.
3. Laptops generated the highest product revenue at **KES 41,535,000**.
4. April recorded the highest monthly revenue of **KES 13,518,300**.
5. Weekday sales accounted for **723 orders**, compared with 277 weekend orders.

### Premium Online Sales Analysis

A targeted analysis filtered high-price-band online transactions from Nairobi and Mombasa.

- Total qualifying records: 83
- Nairobi: 50 orders, KES 6,522,000
- Mombasa: 33 orders, KES 3,696,000
- Combined revenue: KES 10,218,000

The filtered dataset was exported to:

`outputs/premium_online_coast_capital.csv`

## Excel Reporting

The Excel workbook is available at:

`excel/duka_branch_summary.xlsx`

It contains:

- **Sales Data:** Structured sales records in an Excel table named `SalesTable`.
- **Branch Summary:** Branch-level revenue, order counts, units sold, and regional classifications.
- **Region Mapping:** Branch-to-region reference data.
- **Pivot Analysis:** Interactive PivotTable summarizing revenue by branch and sales channel.

The PivotTable uses:
- Rows: Branch
- Columns: Channel
- Values: Sum of revenue

The verified grand total is **KES 71,792,500**.

## Engagement 2: Agent Transaction Data Cleaning

### Dataset Overview

Two datasets were used:

- Agents: 20 records containing agent details.
- Transactions: 612 records containing agent transaction information.

The transaction dataset included issues affecting completeness, consistency, uniqueness, validity, accuracy, and referential integrity.

### Cleaning Activities

The cleaning pipeline implemented the following steps:

1. Removed duplicate transaction IDs.
2. Standardized transaction types.
3. Converted transaction amounts to numeric values.
4. Imputed missing amounts using the median.
5. Flagged potential outliers using the Interquartile Range (IQR) method.
6. Standardized transaction dates.
7. Merged agent information to obtain county details.
8. Identified transactions associated with unknown agents.
9. Generated an audit log documenting the cleaning activities.

### Data Quality Results

| Metric | Result |
|---|---:|
| Original transactions | 612 |
| Duplicate transactions removed | 12 |
| Cleaned transactions | 600 |
| Unique transaction IDs after cleaning | 600 |
| Missing amounts after cleaning | 0 |
| Unknown agent records retained | 7 |
| Potential amount outliers flagged | 53 |

Unknown agent records were retained and identified rather than silently deleted. Their missing county values are expected because the corresponding agent details could not be matched.

### Cleaning Outputs

The cleaned dataset is exported to:

`outputs/agent_transactions_clean.csv`

The cleaning function is implemented in:

`cleaning_pipeline.py`

The complete process and validation are documented in:

`agent_cleanup.ipynb`

## Installation and Execution

### 1. Clone the repository

```bash
git clone https://github.com/Alkhan-019/plp-da-a3-duka-sales-and-agent-cleanup.git
cd plp-da-a3-duka-sales-and-agent-cleanup
```

### 2. Create and activate a virtual environment

On Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Generate the datasets

```bash
python generate_data.py
```

### 5. Run the notebooks

Open the following notebooks in Jupyter Notebook or VS Code:

- `duka_sales_exploration.ipynb`
- `agent_cleanup.ipynb`

Run the cells from top to bottom.

### 6. Review the outputs

Check the `outputs/` folder for the exported CSV files and the `excel/` folder for the Excel report.

## Data Privacy and Protection

This project considers the principles of Kenya's Data Protection Act, 2019.

Good data handling practices include:

- Data minimization: Collect and process only information required for the analytical purpose.
- Purpose limitation: Use data only for its stated analytical purpose.
- Access control: Restrict access to datasets and reports to authorized individuals.
- Data security: Apply appropriate safeguards, including encryption where necessary.
- Retention limitation: Retain information only for as long as necessary.
- Data subject rights: Respect applicable rights of individuals whose personal data is processed.

The generated datasets used in this project are synthetic and do not represent actual customer or agent personal records.

## Technologies Used

- Python
- Pandas
- NumPy
- Jupyter Notebook
- Microsoft Excel
- OpenPyXL
- Git and GitHub

## Conclusion

This project demonstrates the application of data analytics and data quality management to practical business scenarios. The Duka analysis provides insights into sales performance and revenue distribution, while the agent transaction engagement demonstrates a reproducible cleaning pipeline with validation and audit documentation.

The project reinforces the importance of accurate, consistent, complete, and reliable data in business decision-making.
