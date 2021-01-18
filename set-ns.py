
import yaml, os


def main():
    github_ref = os.getenv("GITHUB_REF")
    ref_list = github_ref.split("/")
    if "master" in github_ref:
        branch = ref_list[-1]
        ns = "prod"
    elif "releases" or "features" in github_ref:
        ns = ref_list[-2]+"/"+ref_list[-1]
    else:
        raise Exception("Not valid branch name")

    with open("./file.yaml") as file:
        input = yaml.load(file, Loader=yaml.FullLoader)
    if "ns" in input.keys():
        if ns != input["ns"]:
            raise Exception("You have to edit file.yaml before expect that it can be applied on kubernetes!")
    else:
        input["ns"] = ns
    with open("./file.yaml", "w") as file:
                yaml.dump(input, file)

if __name__ == '__main__':
    main()
