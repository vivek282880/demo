
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

print(documents)