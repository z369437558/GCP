from google.cloud import storage

def make_bucket_public(bucket_name):
    """Makes a bucket and all its objects publicly accessible."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)

    # Get the current IAM policy
    policy = bucket.get_iam_policy(requested_policy_version=3)

    # Add a binding to make all objects in the bucket publicly accessible
    policy.bindings.append({
        "role": "roles/storage.objectViewer",
        "members": {"allUsers"}
    })

    # Set the new IAM policy
    bucket.set_iam_policy(policy)

    print(f"Bucket {bucket.name} is now publicly accessible")

make_bucket_public('ai-lab-video')
