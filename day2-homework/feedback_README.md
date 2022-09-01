Exercise 1: Your annotation is really good! I did have a few minor comments. Check the comments I made in the section below. I tried to make somethings a little clearer

```
for entry in fields[7].split(";"):
# field[7] is the info field. This for loop is splitting the info field by semi-colons, and is then looping through each of the elements in the split info field
    temp = entry.split("=")
    # temp is a single element in the info field (e.x. "AF=1") split at equals, resulting in a list (e.g. ['AF', '1'])
    if len(temp) == 1:
        info[temp[0]] = None
        #explains for elements with no equal signs, the length of temp will be 1 - therefore, there is no equal sign and no data for that id. info is a dictionary that we created previously; if a given id has no associated value, we will add that id to our dictionary (as a key) with the associated value being None
    else:
        name, value = temp
        Type = info_type[name]
        info[name] = type_map[Type](value)
fields[7] = info
```

I also had some comments about the following section:

```
if len(fields) > 8:
#if the length of fields is greater than 8, that means we DO have genotype information
    fields[8] = fields[8].split(":")
    if len(fields[8]) > 1:
    #if the length of index 8 (column 9) is greater than 1, that means there's multiple format flags (e.g. "GT:DP:QL") rather than just one (e.g. "GT")
        for i in range(9, len(fields)):
        # This will loop over fields (i.e. all the information of the entire line) starting at fields[9] and going to the end of the line. This means that we're looping over all of the genotype fields in the line
            fields[i] = fields[i].split(':')
            For a given genotype field, split the genotype information at semi-colons and store this back into "fields" at the correct position
    else:
        fields[8] = fields[8][0]
```
        
Everything else is really really good! Great work!        
        
