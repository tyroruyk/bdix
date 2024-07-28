from bdix.accessibility import accessibility
from bdix.readFile import readFile
from os import path

base_path = path.dirname(path.abspath(__file__))

urls = readFile(
    path.join(base_path, "bdixServers.txt")
)  # credit goes to PC Builder Bangladesh for the server list


def main():
    workingUrls = []
    workingIndexes = [0]
    
    for url in urls:
        if accessibility(url):
            workingUrls.append(url)
            workingIndexes.append(urls.index(url))
    
    workingIndexes.append(0)

    if len(workingUrls) != 0:
        print("List of working servers: ", end=" ")
        for url in workingUrls:
            print(url, end=" ")

        print(
            "\n{0} servers are working out of {1} servers".format(
                len(workingUrls), len(urls)
            )
        )

        print(
            "The working servers also can be found at {0}".format(
                "https://tyroruyk.github.io/bdix/urls?q={0}".format(workingIndexes)
            )
        )

    else:
        print("No server is working :(")

    print("Press any key to quit...", end="")
    input()
