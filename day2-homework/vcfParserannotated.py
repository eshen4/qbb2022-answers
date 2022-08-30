#!/usr/bin/env python3

import sys

def parse_vcf(fname):
    vcf = []
    #establishing vcf as a list that holds the file
    info_description = {}
    #establishes a dictionary, provides information about the headers section of the       vcf file
    info_type = {}
    #establishes a dictionary, provides information on which type of data(?) fields        should be 
    format_description = {}
    #establishes a dictionary, tells us the actual formatting of the overall genotype      information
    type_map = {
        "Float": float,
        "Integer": int,
        "String": str
        }
    #matches the strings in the header info to actual python data values to be able to     use in commands
    malformed = 0
    #initializing a counter for possible errors
#full above block = initalizing variables
    try:
        fs = open(fname)
        #tries to open a file based on name
    except:
        raise FileNotFoundError(f"{fname} does not appear to exist", file=sys.stderr)
        #if file cannot be found, an error should be raised and reported

    for h, line in enumerate(fs):
    #start working through the provided file line by line - h, line are variables, enumerate command tells us to number (creates a tuple of index, thing) the lines within the file. Therefore, this explains that for each line in this provided file, run through the following.
        if line.startswith("#"):
        #this if statement explains what to do with header lines ("#").
            try:
                if line.startswith("##FORMAT"):
                    fields = line.split("=<")[1].rstrip(">\r\n") + ","
                    i = 0
                    start = 0
                    in_string = False
                    while i < len(fields):
                        if fields[i] == "," and not in_string:
                            name, value = fields[start:i].split('=')
                            if name == "ID":
                                ID = value
                            elif name == "Description":
                                desc = value
                            start = i + 1
                        elif fields[i] == '"':
                            in_string = not in_string
                        i += 1
                    format_description[ID] = desc.strip('"')
                elif line.startswith("##INFO"):
                    fields = line.split("=<")[1].rstrip(">\r\n") + ","
                    i = 0
                    start = 0
                    in_string = False
                    while i < len(fields):
                        if fields[i] == "," and not in_string:
                            name, value = fields[start:i].split('=')
                            if name == "ID":
                                ID = value
                            elif name == "Description":
                                desc = value
                            elif name == "Type":
                                Type = value
                            start = i + 1
                        elif fields[i] == '"':
                            in_string = not in_string
                        i += 1
                    info_description[ID] = desc.strip('"')
                    info_type[ID] = Type
                elif line.startswith('#CHROM'):
                    fields = line.lstrip("#").rstrip().split("\t")
                    vcf.append(fields)
            except:
                raise RuntimeError("Malformed header")
        #this try block essentially makes sure things within the header are formatted correctly - hence the exception "Malformed header".
        else:
        #considering the if statement on the header, this else statement leads us to the body of the vcf file.
            try:
            #checks if this variant line is formatted correctly
                fields = line.rstrip().split("\t")
                #on a single line, we are getting rid of trailing characters, and then we are splitting the line by tabs (\t delimiter)
                fields[1] = int(fields[1])
                #makes the second entry within a vcf file an integer. this entry in a vcf file should be the variant position.
                if fields[5] != ".":
                #if position 6 in fields is NOT equal to a period, we perform the following action. position 6 in a vcf file is the quality, and a period will indicate that this information for that line is not there.
                    fields[5] = float(fields[5])
                    #explains that if position 6 is NOT a period, log the information there into a float.
                info = {}
                #forms an empty dictionary for the info field
                for entry in fields[7].split(";"):
                #in vcf file, field 7 is the info field. this command tells that for each entry in the info field, splits the info separated by semicolons into a list.
                    temp = entry.split("=")
                    #temp will be a list of things before and after the equal sign within the current line.
                    if len(temp) == 1:
                        info[temp[0]] = None
                        #explains for info lines with no equal signs, the length of temp will be 1 - therefore, there is no equal sign and no data for that id. info is a dictionary that we created previously; for each time temp has no associated value, that particular key will be recorded into info with id "None".
                    else:
                        name, value = temp
                        Type = info_type[name]
                         #info type dictionary uses the info headers to provide info on  variables. this command allows us to search within the dictionary to search up those variables in the dictionary and assigns them to the variable Type for us to use later.
                        info[name] = type_map[Type](value)
                        #adding a key to the info dictionary we created. type_map[type] pulls out the function associated with that data type. this is used to convert the value within the data field.
                fields[7] = info
                #setting 8th field to be the dictionary we just created.
                if len(fields) > 8:
                #tells us what to do if the file doesn't even have genotype information, referenced to by length being greater than 8
                    fields[8] = fields[8].split(":")
                    #makes a list by splitting information in index 8, 9th column to be separated based on colons; this list is then stored back into the 9th column
                    if len(fields[8]) > 1:
                    #if the length of index 8 (column 9) is greater than 1, aka previous field had information to be split
                        for i in range(9, len(fields)):
                        #loops the split information to be split further starting from field 9
                            fields[i] = fields[i].split(':')
                            #splits the information mentioned above starting from field 9 for the full continuing length of the field
                    else:
                        fields[8] = fields[8][0]
                        #while looking at the 8th index (column 9), grab the first item [0] from the 9th column [8]. basically, if there's only one thing in that list, store it as the first item in said list.
                vcf.append(fields)
                #sticks our giant fields list into our empty vcf list created previously.
            except:
                malformed += 1
            #for all lines that are not formatted in a way that can be processed above, add to our error counter.
    vcf[0][7] = info_description
    if len(vcf[0]) > 8:
    #if there is genotype data present (based on the length of the line):
        vcf[0][8] = format_description
        #sets header line?
    if malformed > 0:
        print(f"There were {malformed} malformed entries", file=sys.stderr)
        #if, based on our previously established error counter, there are errors (counter being >0), print a formatted string (f"there were..."), and then print towards standard error pipeline rather than the output.
    return vcf
    #provides an output from this program that we just ran, allowing us to run this function outside these standards.

if __name__ == "__main__":
    fname = sys.argv[1]
    #sets the filename of the vcf to be this fname variable provided (the first system index)
    vcf = parse_vcf(fname)
    #runs the function on our fname through a stored variable (vcf)
    for i in range(10):
        print(vcf[i])
        #prints our results based on this variable
