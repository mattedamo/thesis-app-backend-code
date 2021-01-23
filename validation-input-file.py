import yaml, os

def main():
    with open("./input.yaml") as file:
        input = yaml.load(file, Loader=yaml.FullLoader)
    if "branch" not in input.keys():
        raise Exception("You have to insert the correct namespace manually into the input yaml file, "+ 
                        "to confirm that you have made the actual changes in it!")
        
    if input["branch"] != (os.environ["GITHUB_REF"].split("/")[-1] || os.environ["GITHUB_REF"].split("/")[-2]+"/"+os.environ["GITHUB_REF"].split("/")[-1] :
        raise Exception("You have to insert the correct namespace manually into the input yaml file, "+ 
                        "to confirm that you have made the actual changes in it!")
    if "clusters" not in input.keys():
        raise Exception("You have to specific the cluster name(s) where you want to deploy the application!")
if __name__ == '__main__':
    main()
