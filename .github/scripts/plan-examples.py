import json
import glob
import re


def get_examples():
    """
    Get all Terraform example root directories using their respective `versions.tf`;
    returning a string formatted json array of the example directories minus those that are excluded
    """
    exclude = {
        'patterns/appmesh-mtls',  # excluded until Rout53 is setup
        'patterns/blue-green-upgrade/environment',
        'patterns/blue-green-upgrade/modules/eks_cluster'
    }

    projects = {
        x.replace('/versions.tf', '')
        for x in glob.glob('patterns/**/versions.tf', recursive=True)
        if not re.match(r'^.+/_', x)
    }

    print(json.dumps(list(projects.difference(exclude))))


if __name__ == '__main__':
    get_examples()
