import os
import yaml

import parser

from github import Github

class Gosplan:
    def __init__(self, organization):
        self.client = Github(os.getenv("ACCESS_TOKEN", default="abc123"))
        self.organization = organization

    def run(self):
        print('STANDBY FOR GOSPLANNING')

        names, gosplans = parser.parse_gosplans()
        
        print('INSTANTIATING GOSPLANS')

        self._create_repos(names, gosplans)

        print('APPLYING GOSPLAN CONFIGURATIONS')

        self._apply_configs(gosplans)

        print('IDENTIFYING NON COMPLIANT SCUM')

        git_repos = self._get_all_repos()
        unplanned_repos = self._identify_unplanned_repos(git_repos, names)
        
        print(f'THE FOLLOWING REPOS WILL BE CLOBBERED -> {unplanned_repos}')

        for repo in unplanned_repos:
            self._upload_dave(repo)
            self._upload_resignation(repo)
            self._clobber_repo(repo)




    # Clobber the offending repo
    def _clobber_repo(self, repo_name):
        repo = self.client.get_repo(f'gosplan/{repo_name}')
        readme_contents = repo.get_contents("README.md")
        repo.update_file(
            readme_contents.path, 
            "YOU MUST COMPLY", 
            "![Image of glory and power](gosplan.png) <br/> ![Image of great sadness and misery](sad_dave.png)", 
            readme_contents.sha, 
            branch="master"
        )

    # Upload the picture of Dave to the offending repository
    def _upload_dave(self, repo_name):
        with open('assets/gosplan.png', 'rb') as image:
            data = image.read()
            repo = self.client.get_repo(f'gosplan/{repo_name}')
            repo.create_file(
                path="gosplan.png",
                branch="master",
                message="YOU HAVE NO POWER",
                content=data
            )
        with open('assets/sad_dave.png', 'rb') as image:
            data = image.read()
            repo = self.client.get_repo(f'gosplan/{repo_name}')
            repo.create_file(
                path="sad_dave.png",
                branch="master",
                message="YOU HAVE NO POWER",
                content=data
            )

    # Upload the resignation letter to the repository
    def _upload_resignation(self, repo_name):
        print('HASTENING THE EXIT OF THE TREACHEROUS SCUM BY UPLOADING MOST HUMBLE, DIGNIFIED AND COMPLIANT RESIGNATION STATEMENT')
        with open('assets/resignation.md', 'rb') as resignation:
                data = resignation.read()
                repo = self.client.get_repo(f'gosplan/{repo_name}')
                repo.create_file(
                    path="I_HAVE_FAILED_IN_MY_DUTY_TO_THIS_GREAT_AND_GLORIOUS_ORGANISATION.md",
                    branch="master",
                    message="I DO NOT DESERVE TO CONTINUE IN YOUR EMPLOYMENT",
                    content=data
                )


    def _get_all_repos(self):
        org = self.client.get_organization(self.organization)
        repos = org.get_repos()
        repo_list = set()
        for repo in repos:
            repo_list.add(repo.name)
        return repo_list
        
    def _identify_unplanned_repos(self, github_repos, gosplan_names):
        return github_repos - gosplan_names


    # Create a new repo based on a GOSPLAN
    def _create_repos(self, names, gosplans):
        org = self.client.get_organization(self.organization)
        for name in names:
            try:
                print(f'Provisioning {name}...')
                plan = gosplans[name]
                org.create_repo(
                    name=plan["name"],
                    private=plan['private']
                )
            except:
                print(f'{name} ALREADY EXISTS - NO FURTHER COMPLIANCE IS REQUIRED. CONTINUE ABOUT YOUR DAILY BUSINESS SAFE IN THE KNOWLEDGE THAT YOU WILL NOT BE CLOBBERED AT THIS TIME.')


    # Apply GOSPLAN config to a repo
    def _apply_configs(self, gosplans):
        print("Applying config...")





