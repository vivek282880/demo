
from llama_index.readers.github import GithubRepositoryReader
from llama_index.readers.github import GithubClient


github_token = "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"

owner = "vivek282880"
repo = "demo"
branch = "main"

documents = GithubRepositoryReader(
    github_client=GithubClient(github_token=github_token),
    owner=owner,
    repo=repo,
    use_parser=False,
    verbose=False
).load_data(branch=branch)

#print(documents)
for i in range(0, len(documents)):
    print(documents[i].get_content())
    details = documents[i].dict()
    print("fileName - ",details.get('metadata').get('file_name'))
    print("=====================================================")