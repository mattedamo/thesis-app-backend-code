
import yaml, os


def main():
    string = "master/release/11"
    print(os.environ.get("GIT_ASKPASS").split("/")[-1])
    branch = string.split("/")[-1]
    branch1 = string.split("/")[-2]
    print(type(int(branch)))
    print(int(branch))
    list = string.split("/")
    newnew = list[-2]+"/"+list[-1]
    print(newnew)
if __name__ == '__main__':
    main()
