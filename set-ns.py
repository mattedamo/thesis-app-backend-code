
import yaml, os


def main():
    github_ref = os.getenv("GITHUB_REF")
    #list = github_ref.split("/")
    if "master" in github_ref:
        ns = "prod"
    elif "releases" or "features" in github_ref:
        ns = github_ref
    else:
        raise Exception("Not valid branch name")

    with open("./file.yaml") as file:
        input = yaml.load(file, Loader=yaml.FullLoader)
    if "ns" in input.keys():
        ns = { "ns" : ns }
        input.update(ns)
    else:
        input["ns"] = ns
    with open("./file.yaml", "w") as file:
                yaml.dump(input, file)

if __name__ == '__main__':
    main()
