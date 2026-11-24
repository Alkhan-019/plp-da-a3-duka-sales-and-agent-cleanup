
import pandas as pd


def clean_agent_data(txns, agents):
    """
    Clean agent transaction data, merge agent details,
    and return the cleaned dataset with an audit log.

    Cleaning operations:
    1. Remove duplicate transaction IDs.
    2. Standardize transaction types.
    3. Convert amounts to numeric values.
    4. Impute missing or invalid amounts.
    5. Flag potential amount outliers.
    6. Standardize transaction dates.
    7. Merge agent county information.
    8. Identify transactions with unknown agents.

    Returns:
        clean_df: Cleaned transaction DataFrame.
        log: DataFrame containing cleaning audit details.
    """

    clean_df = txns.copy()
    agents_df = agents.copy()
    audit_log = []

    # 1. Remove duplicate transactions using txn_id
    duplicates = clean_df.duplicated(
        subset="txn_id", keep="first"
    )
    duplicate_count = int(duplicates.sum())

    clean_df = clean_df.loc[~duplicates].copy()

    audit_log.append({
        "issue": "Duplicate transactions removed",
        "dimension": "Uniqueness",
        "column": "txn_id",
        "rows_affected": duplicate_count
    })

    # 2. Standardize transaction types
    original_types = clean_df["txn_type"].copy()

    clean_df["txn_type"] = (
        clean_df["txn_type"]
        .astype("string")
        .str.strip()
        .str.lower()
        .str.capitalize()
    )

    type_changes = int(
        (original_types != clean_df["txn_type"]).sum()
    )

    audit_log.append({
        "issue": "Transaction types standardized",
        "dimension": "Consistency",
        "column": "txn_type",
        "rows_affected": type_changes
    })

    # 3. Convert transaction amounts to numeric
    original_amounts = clean_df["amount"].copy()

    clean_df["amount"] = pd.to_numeric(
        clean_df["amount"],
        errors="coerce"
    )

    invalid_amounts = int(
        (original_amounts.notna() & clean_df["amount"].isna()).sum()
    )

    audit_log.append({
        "issue": "Invalid amounts converted to missing values",
        "dimension": "Validity",
        "column": "amount",
        "rows_affected": invalid_amounts
    })

    # 4. Impute missing amounts using the transaction median
    missing_amounts = clean_df["amount"].isna()

    clean_df["amount_imputed"] = missing_amounts

    missing_count = int(missing_amounts.sum())

    if missing_count > 0:
        median_amount = clean_df["amount"].median()

        clean_df["amount"] = clean_df["amount"].fillna(
            median_amount
        )

    audit_log.append({
        "issue": "Missing amounts imputed using median",
        "dimension": "Completeness",
        "column": "amount",
        "rows_affected": missing_count
    })

    # 5. Flag potential outliers using the IQR method
    q1 = clean_df["amount"].quantile(0.25)
    q3 = clean_df["amount"].quantile(0.75)
    iqr = q3 - q1

    lower_bound = q1 - (1.5 * iqr)
    upper_bound = q3 + (1.5 * iqr)

    clean_df["is_outlier"] = (
        (clean_df["amount"] < lower_bound)
        | (clean_df["amount"] > upper_bound)
    )

    outlier_count = int(clean_df["is_outlier"].sum())

    audit_log.append({
        "issue": "Potential amount outliers flagged",
        "dimension": "Accuracy",
        "column": "amount",
        "rows_affected": outlier_count
    })

    # 6. Standardize transaction dates
    original_dates = clean_df["txn_date"].copy()

    clean_df["txn_date"] = pd.to_datetime(
        clean_df["txn_date"],
        errors="coerce",
        format="mixed"
    )

    invalid_dates = int(
        clean_df["txn_date"].isna().sum()
    )

    clean_df["txn_date"] = clean_df["txn_date"].dt.strftime(
        "%Y-%m-%d"
    )

    date_changes = int(
        (
            original_dates.astype("string")
            != clean_df["txn_date"].astype("string")
        ).sum()
    )

    audit_log.append({
        "issue": "Transaction dates standardized",
        "dimension": "Consistency",
        "column": "txn_date",
        "rows_affected": date_changes
    })

    # 7. Merge agent county information
    clean_df = clean_df.merge(
        agents_df[["agent_id", "county"]],
        on="agent_id",
        how="left",
        validate="many_to_one",
        indicator=True
    )

    unknown_agents = int(
        (clean_df["_merge"] == "left_only").sum()
    )

    clean_df["agent_match_status"] = clean_df["_merge"].map({
        "both": "Matched",
        "left_only": "Unknown agent",
        "right_only": "Unused agent"
    })

    clean_df.drop(columns=["_merge"], inplace=True)

    audit_log.append({
        "issue": "Transactions with unknown agents identified",
        "dimension": "Referential Integrity",
        "column": "agent_id",
        "rows_affected": unknown_agents
    })

    # 8. Create audit log
    log = pd.DataFrame(audit_log)

    return clean_df, log
