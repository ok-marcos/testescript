import git

repo = git.Repo(
    'Dockerfile')
# print("Test 1 2 3 ")

# remoteurl = "https://github.com/ok-marcos/repo-java/blob/master/Dockerfile"
# localfolder = "temp/galpaomarinha"

repo.remotes.origin.pull()
# myrepo = git.Repo.clone(remoteurl, localfolder)
# myrepo.git.checkout("master")
