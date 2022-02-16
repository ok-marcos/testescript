from git import Repo

PATH_OF_GIT_REPO = "https://github.com/ok-marcos/galpaodamarinha.git"
COMMIT_MESSAGE = 'teste'


def git_push():
    # try:
    repo = Repo(
        "C:/Users/marcos.silva/Desktop/tdm_testing/10112022/git_repo/temp")
    repo.git.add('--all')
    repo.index.commit('IGOR DAS MENINAS')
    origin = repo.remote(name='origin')
    origin.push().raise_if_error()
    # except:
    #     print('ocorreu um erro')


git_push()
