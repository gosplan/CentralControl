import os
import yaml

from github import Github

class GitClient:
    def __init__(self):
        self.client = Github(os.getenv("ACCESS_TOKEN", default="abc123"))


    # Clobber the offending repo
    def clobber_repo(self, repo_path):
        repo = self.client.get_repo(repo_path)
        readme_contents = repo.get_contents("README.md")
        repo.update_file(
            readme_contents.path, 
            "YOU MUST COMPLY", 
            "![Image of glory and power](sad_dave.png)", 
            readme_contents.sha, 
            branch="master"
        )

    # Upload the picture of Dave to the offending repository
    def _upload_dave(self, repo_path):
        with open('assets/gosplan.png', 'rb') as image:
            data = image.read()
            repo = self.client.get_repo(repo_path)
            repo.create_file(
                path="sad_dave.png",
                branch="master",
                message="YOU HAVE NO POWER",
                content=data
            )

    # Upload the resignation letter to the repository
    def _upload_resignation(self, repo_path):
        print('Uploading resignation letter')


    # Create a new repo based on a GOSPLAN
    def create_repo(self, gosplan):
        print('Provisioning repo...')
        
        user = self.client.get_user()
        user.create_repo(
            name="THIS IS A TEST",
            private=False
        )


    # Apply GOSPLAN config to a repo
    def apply_config(self, gosplan):
        print("Applying config...")



