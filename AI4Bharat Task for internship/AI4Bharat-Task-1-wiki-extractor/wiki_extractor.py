from wiki_api import Wikipedia_info

keyword=input("Enter keyword: ")

n_urls=int(input("no. of url: "))

output=input("Enter filename: ")

obj=Wikipedia_info(keyword,n_urls)

json_data=obj.output_builder()

with open(output, "w") as outfile:
    outfile.write(json_data)
outfile.close()
