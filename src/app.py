from accessibility import accessibility
from readFile import readFile
from os import path
base_path = path.dirname(path.abspath(__file__))

urls = readFile(
    path.join(base_path,"bdixServers.txt")
)  # credit goes to PC Builder Bangladesh for the server list
workingUrls = []

for url in urls:
    if accessibility(url):
        workingUrls.append(url)

if len(workingUrls) != 0:
    print("List of working servers: ", end=" ")
    for url in workingUrls:
        print(url, end=" ")

    print(
        "\n{0} servers are working out of {1} servers".format(
            len(workingUrls), len(urls)
        )
    )

else:
    print("No server is working :(")

print("Press any key to quit...", end="")
input()
