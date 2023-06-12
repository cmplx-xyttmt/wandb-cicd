from ghapi.all import GhApi
import os

api = GhApi(owner='cmplx-xyttmt', repo='wandb-cicd')

pr_number = os.getenv('PR_NUMBER', 1)

api.issues.create_label(name='custom-label', color='00ff00', description='A custom label, since the bug label already exists.')

api.issues.add_labels(pr_number, labels=['bug', 'custom-label'])

comment = api.issues.create_comment(pr_number, 'Labeled this PR as a bug fix.')

print('View comment: ', comment.html_url)
