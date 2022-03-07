from temp.caminho import caminho
from git import Repo


arquivo_up = caminho.caminho_novo
PATH_OF_GIT_REPO = "https://stash.pontoslivelo.com.br/scm/tdmscrip/tdm_scripts_teste.git"
COMMIT_MESSAGE = 'teste'


def git_push():
    # try:
    caminho.executescript()
    repo = Repo(".")
    repo.git.add('--all')
    repo.index.commit('Repositorio Java')
    origin = repo.remote(name='origin')
    origin.push().raise_if_error()
    # except:
    #     print('ocorreu um erro')


git_push()
