import sys

# Check if the script was called with the correct number of arguments
entry = sys.argv
print(len(sys.argv))

if len(sys.argv) != 10:
    print("Usage: python receiving_script.py arg1 arg2 arg3 arg4 arg5 arg6 arg7")
    sys.exit(1)

# Retrieve the values from the command line arguments
arg1 = sys.argv[1]
arg2 = sys.argv[2]
arg3 = sys.argv[3]
arg4 = sys.argv[4]
arg5 = sys.argv[5]
arg6 = sys.argv[6]
arg7 = sys.argv[7]
arg8 = sys.argv[8]
arg9 = sys.argv[9]

# Print the values
print(f"Argument 1: {arg1}")
print(f"Argument 2: {arg2}")
print(f"Argument 3: {arg3}")
print(f"Argument 4: {arg4}")
print(f"Argument 5: {arg5}")
print(f"Argument 6: {arg6}")
print(f"Argument 7: {arg7}")
print(f"Argument 8: {arg8}")
print(f"Argument 9: {arg9}")

# Login to the gmail account
gmail_login = "devinci.fablab.automation@gmail.com"
gmail_pass = "DVFL2020*"

#TODO : Transform the output so that the user receives a mail with the signature directly in the body of the mail
# Pour le moment, le script crée un fichier signature.html dans le dossier courant






# Using the values to setup the signature



