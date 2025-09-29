import pandas as pd
from datetime import datetime

# Example deployment log data (replace with real CI/CD logs)
data = [
    {"commit_id": "a1", "deployed": True, "deploy_time": "2025-09-01 10:00", "failed": False, "recovered_time": None},
    {"commit_id": "a2", "deployed": True, "deploy_time": "2025-09-02 12:00", "failed": True, "recovered_time": "2025-09-02 13:00"},
    {"commit_id": "a3", "deployed": True, "deploy_time": "2025-09-03 09:00", "failed": False, "recovered_time": None},
    {"commit_id": "a4", "deployed": True, "deploy_time": "2025-09-04 15:00", "failed": False, "recovered_time": None},
    {"commit_id": "a5", "deployed": True, "deploy_time": "2025-09-05 11:00", "failed": True, "recovered_time": "2025-09-05 12:00"},
]
df = pd.DataFrame(data)

def deployment_frequency(df):
    # Number of deployments per week
    df['week'] = pd.to_datetime(df['deploy_time']).dt.isocalendar().week
    freq = df.groupby('week').size()
    return freq

def lead_time_for_changes(df):
    # Simulate lead time (replace with real commit-to-deploy times)
    # Here, just use deploy_time as a placeholder
    lead_times = [1.5, 2.0, 1.0, 2.5, 1.2]  # Example in hours
    return pd.Series(lead_times, name='lead_time_hours')

def change_failure_rate(df):
    # Percentage of failed deployments
    total = len(df)
    failed = df['failed'].sum()
    return (failed / total) * 100

def mean_time_to_recovery(df):
    # Average time to recovery for failed deployments
    mttr = []
    for _, row in df[df['failed']].iterrows():
        start = datetime.strptime(row['deploy_time'], '%Y-%m-%d %H:%M')
        end = datetime.strptime(row['recovered_time'], '%Y-%m-%d %H:%M')
        mttr.append((end - start).total_seconds() / 60)  # in minutes
    return sum(mttr) / len(mttr) if mttr else 0

if __name__ == "__main__":
    print("Deployment Frequency (per week):")
    print(deployment_frequency(df))
    print("\nLead Time for Changes (hours):")
    print(lead_time_for_changes(df))
    print(f"\nChange Failure Rate: {change_failure_rate(df):.2f}%")
    print(f"\nMean Time to Recovery (MTTR): {mean_time_to_recovery(df):.2f} minutes")
