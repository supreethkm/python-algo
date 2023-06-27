def honai(disks, source, helper, destination):
    if disks == 1:
        print("Disks {} moved from {} to {}".format(disks, source, destination))
        return
    
    honai(disks-1, source, destination, helper)
    print("Disks {} moved from {} to {}".format(disks, source, destination))
    honai(disks-1, helper, source, destination)

disks = int(input("Enter number of disks \t"))

honai(disks,"A","B","C")
