def output_repo_names(repo_names):
    print("\n\nFolgende Repositories wurden gefunden:")
    for repo_name in repo_names:
        print(repo_name)


def output_repo_created(repo_name):
    print(f"\n\nRepository {repo_name} wurde erfolgreich erstellt")


def output_error(error_message):
    raise Exception("Bekam Error an folgender Stelle:" + error_message)
