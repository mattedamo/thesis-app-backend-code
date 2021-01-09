import yaml, os


def main():
    
    if os.path.exists("input_params.yaml"):
        os.remove("input.params.yaml")
    
    open("./input_params.yaml", "x")
    print(os.environ)
    
    """
    if "ns" in input.keys():
        ns = { "ns" : os.getenv("NS") }
        input.update(ns)
    else:
        input["ns"] = os.getenv("NS")
    print(os.getenv("NS"))
    print(input)
    with open("./file.yaml", "w") as file:
                yaml.dump(input, file)
    """

if __name__ == '__main__':
    main()
