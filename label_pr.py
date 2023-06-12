from ghapi.all import GhApi
import os

api = GhApi(owner='cmplx-xyttmt', repo='wandb-cicd')

pr_number = os.getenv('PR_NUMBER', 1)

api.issues.create_label(name='bug', color='ff0000', description='A label indicating a bug fix PR.')

api.issues.add_labels(pr_number, labels=['bug'])

comment = api.issues.create_comment('Labeled this PR as a bug fix.')

print('View comment: ', comment.html_url)
