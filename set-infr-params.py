import yaml, os


def main():
    
    if os.path.exists("input_params.yaml"):
        os.remove("input.params.yaml")
    
    open("./input_params.yaml", "x")
    ref = os.getenv("GITHUB_REF")
    tmp_list = ref.split("/")
    branch = tmp_list[-1]
    #devo settare il branch e il nome della kustomize folder
    dic = {}
    dic["branch"] = branch

    if "master" in branch:
        dic["kustomize-dir"] = "prod"
    elif "release" in branch:
        dic["kustomize-dir"] = "test"
    elif "feature" in branch: 
        dic["kustomize-dir"] = "dev"
    else:
        raise Exception('branch name not valid!')

    with open("./input_params.yaml", "w") as file:
                yaml.dump(dic, file)
    
    
if __name__ == '__main__':
    main()
