print(
    """
    ----------------------------------------------------------------
    |HTML Section Generator By Ryothom  Original By WBPRO          |
    |--------------------------------------------------------------|
    |Totally not stolen btw                                        |
    ----------------------------------------------------------------
    """
)


# Tells the generator how many cells in each row
Content = [2,2,2]

# The filename the generators will use
# if you dont add .html it will be automagically append it to the filename
FileName = "Index.html"

# Sets what gets writtten into the Title Attribute
Title = "Testing..."

# Dont mess with these they are indent levels for the generator
Lv1 = "  "
Lv2 = "      "
Lv3 = "         "


# Automagically append .html to the filename if not present
if str.lower(".html") in FileName:
    print("[LOG] .html already in filename. Leaving it alone.")
else:
    FileName = FileName + ".html"
    print("[LOG] .html is not in filename(you lazy son of a bitch) appending it!")


def WriteHeaders():
    """
    Write proper metadata to the begining of the file.
    """
    # This is ugly as fuck but its 2am what are u gonna do?
    MetaData = f"""<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{Title}</title>
    </head>
    <body>
        """

    # Create a Context Manager 
    # This make handling errors easier 
    # and make sure our file is close porperly every time
    with open(FileName, "w+") as FileHandle:
        FileHandle.write(MetaData)
        GenerateTable(FileHandle, Content)
        FileHandle.close()
        return

def GenerateTable(FileHandle, Content):
    """
    Generate the table in a pretty jank
    yet suprisingly flexible way
    (its 2:30am at this point)
    """
    FileHandle.write("\n")
    FileHandle.write('<form>')
    
    # Generate Markup
    # Theres probably a cleaner implementation but i dont have time
    for sections in Content:

        print(f"[LOG] Writing Section No.{sections}")

        FileHandle.write(f"\n{Lv2}<section class="">")
        if Content[0] == sections:
            for i in range(sections):
                print(f"[LOG] Writing label No.{i}")
                FileHandle.write(f"\n{Lv1}<label for=>PlaceHolder{i}</label>") 
                FileHandle.write(f"\n{Lv1}<input type= name= id=>")
            
            print("[LOG] Writing Section Close Tag")
            FileHandle.write(f"\n{Lv2}</section>")
        
        else:
            for i in range(sections):
                    print(f"[LOG] Writing data tag No.{i}")
                    FileHandle.write(f"\n{Lv3}<label for=>PlaceHolder{i}</td>") 

    print("[LOG] Writing Form Close Tag")
    FileHandle.write("\n</form>")

    # Return at the end of this mess
    return 


def WriteCloseTags(FileHandle):
    """
    Writes body and html close tags to the end of the file
    """
    FileHandle.write("\n</body>")
    FileHandle.write("\n</html>")
    return

def Main():
    WriteHeaders()
    print("[LOG] All Done!")
    return

if __name__ == "__main__":
    # If we are not running as an import call the main function
    Main()

    # if done exit
    print("[LOG] Exiting!")
    exit(0)